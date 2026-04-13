var fso = new ActiveXObject("Scripting.FileSystemObject");
var f = fso.OpenTextFile("quiz_data_test.js", 1);
var content = f.ReadAll();
f.Close();

try {
    eval(content);
    WScript.Echo("Syntax is OK!");
} catch (e) {
    WScript.Echo("Syntax Error:");
    WScript.Echo(e.message);
    // WScript errors don't always give line numbers directly easily without more context,
    // but message might help.
}
