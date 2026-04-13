import sys

content = """    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // GSAP Entrance Animation
            const tl = gsap.timeline({
                defaults: { duration: 1.5, ease: "power4.out" }
            });

            // Set initial positions (exploded state)
            gsap.set('#redTop .logo-path', { y: -100, opacity: 0, scale: 0.5, rotation: -20 });
            gsap.set('#redLeft .logo-path', { x: -100, opacity: 0, scale: 0.5, rotation: 20 });
            gsap.set('#blueBottom .logo-path', { y: 100, opacity: 0, scale: 0.5, rotation: 10 });
            gsap.set('#blueRight .logo-path', { x: 100, opacity: 0, scale: 0.5, rotation: -10 });

            // Assemble the logo
            tl.to('.logo-path', {
                opacity: 1,
                x: 0,
                y: 0,
                rotation: 0,
                scale: 1,
                stagger: {
                    each: 0.05,
                    from: "center"
                }
            }, "+=0.3");

            // Floating "Antigravity" Effect
            gsap.to('#logo-svg', {
                y: -15,
                duration: 4,
                repeat: -1,
                yoyo: true,
                ease: "sine.inOut"
            });

            // Interactive Parallax
            window.addEventListener('mousemove', (e) => {
                const { clientX, clientY } = e;
                const moveX = (clientX - window.innerWidth/2) / (window.innerWidth/2);
                const moveY = (clientY - window.innerHeight/2) / (window.innerHeight/2);

                gsap.to('.red-layer', {
                    x: moveX * 20,
                    y: moveY * 20,
                    duration: 0.8,
                    ease: "power2.out"
                });

                gsap.to('.blue-layer', {
                    x: moveX * 12,
                    y: moveY * 12,
                    duration: 1,
                    ease: "power2.out"
                });
            });
        });
    </script>"""

with open('marian_analytics.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the indices of the first <script> after line 400 and the last </html>
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if i > 460 and '<script>' in line:
        start_idx = i
        break

for i, line in enumerate(lines):
    if i > start_idx and '</html>' in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_lines = lines[:start_idx] + [content + '\n'] + lines[end_idx:]
    with open('marian_analytics.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Successfully patched marian_analytics.html")
else:
    print(f"Error: Could not find markers. Start: {start_idx}, End: {end_idx}")
    sys.exit(1)
