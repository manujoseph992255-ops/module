function doGet(e) {
  var action = e.parameter.action;
  var callback = e.parameter.callback;

  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName("Login") || ss.getActiveSheet();
    var data = sheet.getDataRange().getValues();

    // 1. REGISTER ACTION
    if (action === "register" || action === "signup") {
      var name = e.parameter.name || "Unknown";
      var gmail = e.parameter.gmail || e.parameter.email || "Missing"; // FOOLPROOF: check both
      var phone = e.parameter.phone || "";
      var code = e.parameter.classCode || e.parameter.code || "None";
      var pass = e.parameter.password || "";

      if (!phone) return finalize(callback, {success: false, error: "Phone number is required"});

      // Check if phone exists (Column B = index 1)
      for (var i = 1; i < data.length; i++) {
        if (data[i][1] && data[i][1].toString().trim() === phone.toString().trim()) {
          return finalize(callback, {success: false, error: "Phone number already exists"});
        }
      }

      // Record Order: Name(A), Phone(B), Class(C), Gmail(D), Password(E)
      sheet.appendRow([name, phone, code, gmail, pass]);
      
      return finalize(callback, {
        success: true, 
        message: "Recorded: " + gmail + " (Col D)",
        debug: "Name: " + name + ", Phone: " + phone + ", Gmail: " + gmail
      });
    }

    // 2. LOGIN ACTION
    if (action === "login") {
      var phone = e.parameter.phone || "";
      var pass = e.parameter.password || "";
      for (var i = 1; i < data.length; i++) {
        var rowPhone = data[i][1] ? data[i][1].toString().trim() : "";
        var rowPass = data[i][4] ? data[i][4].toString().trim() : "";
        if (rowPhone === phone.toString().trim() && rowPass === pass.toString().trim()) {
          return finalize(callback, {
            exists: true, 
            success: true, 
            name: data[i][0],
            classCode: data[i][2] || "",
            gmail: data[i][3] || ""
          });
        }
      }
      return finalize(callback, {exists: false, success: false, error: "Incorrect Phone or Password"});
    }

    // 3. RECOVER ACTION
    if (action === "recover") {
      var phone = e.parameter.phone || "";
      for (var i = 1; i < data.length; i++) {
        var rowPhone = data[i][1] ? data[i][1].toString().trim() : "";
        if (rowPhone === phone.toString().trim()) {
          return finalize(callback, {recovered: true, success: true});
        }
      }
      return finalize(callback, {recovered: false, success: false, error: "Phone not found"});
    }

    // 4. RESET ACTION
    if (action === "reset") {
      var phone = e.parameter.phone || "";
      var newPass = e.parameter.password || "";
      for (var i = 1; i < data.length; i++) {
        var rowPhone = data[i][1] ? data[i][1].toString().trim() : "";
        if (rowPhone === phone.toString().trim()) {
          sheet.getRange(i + 1, 5).setValue(newPass);
          return finalize(callback, {success: true});
        }
      }
      return finalize(callback, {success: false, error: "Reset failed"});
    }

    // 5. SUBMIT SCORE ACTION
    if (action === "submitScore") {
      var phone = e.parameter.phone || "";
      var name = e.parameter.name || "Unknown";
      var score = e.parameter.score || "0";
      var moduleID = e.parameter.moduleID || ""; 
      var classCode = e.parameter.classCode || "";
      var gmail = e.parameter.gmail || "";
      var startTime = e.parameter.startTime || null;
      
      if (!phone) return finalize(callback, {success: false, error: "Phone required"});

      var resSheet = ss.getSheetByName("Results");

      var headers = [
        "Phone Number", "Name", "Class Code", "Email ID",
        "Module-1", "Timestamp-1",
        "Module-2", "Timestamp-2",
        "Module-3", "Timestamp-3",
        "Module-4", "Timestamp-4",
        "Module-5", "Timestamp-5",
        "Module-6", "Timestamp-6",
        "Mock-1", "Timestamp-Mock-1",
        "Mock-2", "Timestamp-Mock-2"
      ];

      if (!resSheet) {
        resSheet = ss.insertSheet("Results");
        resSheet.appendRow(headers);
        resSheet.getRange(1, 1, 1, headers.length).setFontWeight("bold").setBackground("#f3f3f3");
        resSheet.setFrozenRows(1);
      }

      if (!classCode || !gmail) {
        var loginSheet = ss.getSheetByName("Login");
        if (loginSheet) {
          var loginData = loginSheet.getDataRange().getValues();
          for (var i = 1; i < loginData.length; i++) {
            if (loginData[i][1] && loginData[i][1].toString().trim() === phone.toString().trim()) {
              if (!classCode) classCode = loginData[i][2] || ""; 
              if (!gmail) gmail = loginData[i][3] || ""; 
              break;
            }
          }
        }
      }

      var resData = resSheet.getDataRange().getValues();
      var rowIndex = -1;
      for (var j = 1; j < resData.length; j++) {
        if (resData[j][0] && resData[j][0].toString().trim() === phone.toString().trim()) {
          rowIndex = j + 1;
          break;
        }
      }

      var now = new Date();
      var timeValue = Utilities.formatDate(now, "GMT+5:30", "yyyy-MM-dd HH:mm:ss"); // Default to timestamp if no startTime
      if (startTime) {
        var totalSeconds = Math.round((now.getTime() - parseInt(startTime)) / 1000);
        var mins = Math.floor(totalSeconds / 60);
        var secs = totalSeconds % 60;
        timeValue = mins + " min " + secs + " sec";
      }

      var scoreCol, timeCol;
      if (moduleID.startsWith("mock")) {
        var num = moduleID.replace("mock", "");
        if (num === "1") { scoreCol = 17; timeCol = 18; }
        else if (num === "2") { scoreCol = 19; timeCol = 20; }
        else return finalize(callback, {success: false, error: "Invalid Mock ID"});
      } else {
        var num = parseInt(moduleID);
        if (!isNaN(num) && num >= 1 && num <= 6) {
          scoreCol = (num - 1) * 2 + 5;
          timeCol = (num - 1) * 2 + 6;
        } else {
          return finalize(callback, {success: false, error: "Invalid Module ID"});
        }
      }

      if (rowIndex === -1) {
        var newRow = new Array(headers.length).fill("");
        newRow[0] = phone;
        newRow[1] = name;
        newRow[2] = classCode;
        newRow[3] = gmail;
        newRow[scoreCol - 1] = score;
        newRow[timeCol - 1] = timeValue;
        resSheet.appendRow(newRow);
      } else {
        resSheet.getRange(rowIndex, scoreCol).setValue(score);
        resSheet.getRange(rowIndex, timeCol).setValue(timeValue);
        resSheet.getRange(rowIndex, 3).setValue(classCode);
        resSheet.getRange(rowIndex, 4).setValue(gmail);
        resSheet.getRange(rowIndex, 2).setValue(name);
      }

      return finalize(callback, {success: true, message: "Score and time updated for " + moduleID});
    }

    return finalize(callback, {success: false, error: "Invalid Action"});

  } catch (err) {
    return finalize(callback, {success: false, error: "Script Error: " + err.message});
  }
}

function finalize(callback, data) {
  var out = JSON.stringify(data);
  if (callback) {
    return ContentService.createTextOutput(callback + "(" + out + ")").setMimeType(ContentService.MimeType.JAVASCRIPT);
  }
  return ContentService.createTextOutput(out).setMimeType(ContentService.MimeType.JSON);
}
