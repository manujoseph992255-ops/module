var fs = new ActiveXObject("Scripting.FileSystemObject");
var f = fs.OpenTextFile("quiz_data.js", 1);
var content = f.ReadAll();
f.Close();

try {
    eval(content);
    WScript.Echo("Syntax is valid!");
} catch (e) {
    WScript.Echo("Syntax Error: " + e.message + " at line " + e.line);
}
