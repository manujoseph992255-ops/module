var fs = new ActiveXObject("Scripting.FileSystemObject");
var f = fs.OpenTextFile("quiz_data.js", 1);
var content = f.ReadAll();
f.Close();

// Replace const with var to avoid ES3 errors in WSH
content = content.replace("const quizData = {", "var quizData = {");

try {
    eval(content);
    WScript.Echo("Syntax is valid!");
} catch (e) {
    WScript.Echo("Syntax Error: " + e.message + " at line " + e.line);
}
