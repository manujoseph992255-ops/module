import os
import re

files = ["Module-1.html", "Module-3.html", "Module-4.html", "Module-5.html", "Module-6.html"]
directory = r"c:\Users\kj anand\Downloads\Quiz DD"

new_run_skulpt = """        function runSkulpt(id, expected) {
            const prog = document.getElementById(`coding-ans-${id}`).value;
            const outputDiv = document.getElementById(`coding-output-${id}`);
            const feedback = document.getElementById(`coding-feedback-${id}`);
            
            outputDiv.innerHTML = "";
            outputDiv.classList.add('active');
            feedback.style.display = "none";
            feedback.className = "feedback";

            let outputText = "";
            
            Sk.configure({
                output: function(text) { 
                    outputDiv.appendChild(document.createTextNode(text));
                    outputDiv.scrollTop = outputDiv.scrollHeight;
                    outputText += text; 
                },
                read: function(x) {
                    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
                        throw "File not found: '" + x + "'";
                    return Sk.builtinFiles["files"][x];
                },
                input: function(prompt) {
                    return new Promise((resolve) => {
                        const container = document.createElement('div');
                        container.className = 'colab-input-container';
                        container.innerHTML = `
                            <span class="colab-prompt">${prompt}</span>
                            <input type="text" class="colab-input" autocomplete="off">
                        `;
                        outputDiv.appendChild(container);
                        
                        const inputField = container.querySelector('.colab-input');
                        inputField.focus();
                        
                        inputField.addEventListener('keydown', (e) => {
                            if (e.key === 'Enter') {
                                const val = inputField.value;
                                container.remove();
                                outputDiv.appendChild(document.createTextNode(prompt + val + "\\n"));
                                outputText += prompt + val + "\\n";
                                resolve(val);
                            }
                        });
                    });
                }
            });

            const myPromise = Sk.misceval.asyncToPromise(function() {
                return Sk.importMainWithBody("<stdin>", false, prog, true);
            });

            myPromise.then(function(mod) {
                if (!outputDiv.innerHTML) outputDiv.innerText = outputText;
                
                const cleanOutput = outputText.trim().toLowerCase();
                const cleanExpected = expected.trim().toLowerCase();

                if (cleanOutput.includes(cleanExpected)) {
                    feedback.innerHTML = "✓ Correct! Your code works perfectly. 🎉";
                    feedback.className = "feedback correct";
                    triggerConfetti();
                } else {
                    feedback.innerHTML = `✗ Wrong! Expected to see "${expected}" in output.`;
                    feedback.className = "feedback wrong";
                }
                feedback.style.display = "block";
            }, function(err) {
                outputDiv.innerText += "\\n" + err.toString();
                feedback.innerHTML = "✗ Error in your code!";
                feedback.className = "feedback wrong";
                feedback.style.display = "block";
            });
        }"""

# Improved regex to capture the whole function regardless of variations in the middle
pattern = re.compile(r"function runSkulpt\(id, expected\)\s*\{(?:[^{}]*|\{[^{}]*\})*\}", re.DOTALL)

for filename in files:
    path = os.path.join(directory, filename)
    if not os.path.exists(path):
        print(f"File {filename} not found.")
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the existing runSkulpt function
    new_content = pattern.sub(new_run_skulpt, content)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes made to {filename} (pattern might not have matched)")
