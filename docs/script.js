// Terminal demo animation
document.addEventListener('DOMContentLoaded', function() {
    const terminalOutput = document.getElementById('terminal-output');
    const terminalElement = document.getElementById('demo-terminal');
    
    // Demo session content
    const demoSession = [
        '$ python cybertoolkit.py',
        'Welcome to CyberToolkit',
        '1. Port Scanner',
        '2. Banner Grabber',
        '3. File Hash',
        '4. DNS Lookup',
        '5. Password Generator',
        '6. Exit',
        'Select a tool: 1',
        'Scanning host: 192.168.1.1',
        'Port 80: open',
        'Port 443: open',
        'Port 22: closed',
        'Scan complete.',
        '$ python cybertoolkit.py -s 192.168.1.1 80-100',
        'Scanning ports 80-100 on 192.168.1.1',
        'Port 80: open',
        'Port 443: open',
        'Port 8080: open',
        'Scan complete.',
        '$ python cybertoolkit.py -d google.com',
        'google.com resolves to: 142.250.191.14',
        '$ python cybertoolkit.py -f example.txt',
        'SHA-256 hash: a1b2c3d4e5f67890123456789012345678901234567890123456789012345678',
        '$ python cybertoolkit.py -p 16',
        'Generated password: XyZ7$mN9@pQ2!rS4',
        '$'
    ];
    
    let currentIndex = 0;
    let currentLine = '';
    let typingSpeed = 30; // milliseconds per character
    
    function typeNextLine() {
        if (currentIndex < demoSession.length) {
            const line = demoSession[currentIndex];
            currentLine = '';
            typeCharacter();
        } else {
            // Reset to start the demo again after completion
            setTimeout(() => {
                terminalOutput.innerHTML = '';
                currentIndex = 0;
                typeNextLine();
            }, 3000);
        }
    }
    
    function typeCharacter() {
        if (currentIndex < demoSession.length) {
            const line = demoSession[currentIndex];
            
            if (currentLine.length < line.length) {
                currentLine += line[currentLine.length];
                terminalOutput.textContent += line[currentLine.length - 1];
                
                // Add cursor effect
                if (currentLine[currentLine.length - 1] === '$') {
                    terminalOutput.textContent += ' ';
                }
                
                // Add cursor at the end of line
                if (currentLine.length === line.length) {
                    terminalOutput.textContent += '\n';
                }
                
                setTimeout(typeCharacter, typingSpeed);
            } else {
                // Move to next line after delay
                setTimeout(() => {
                    currentIndex++;
                    typeNextLine();
                }, 500); // Wait a bit before next line
            }
        }
    }
    
    // Check if user prefers reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    
    if (!prefersReducedMotion) {
        // Start the typing animation after a delay
        setTimeout(() => {
            typeNextLine();
        }, 1000);
    } else {
        // Show complete demo for reduced motion users
        demoSession.forEach((line, index) => {
            if (index > 0) terminalOutput.textContent += '\n';
            terminalOutput.textContent += line;
        });
    }
    
    // Add copy buttons for code snippets
    const codeSnippets = document.querySelectorAll('pre code');
    codeSnippets.forEach(snippet => {
        const copyButton = document.createElement('button');
        copyButton.textContent = 'Copy';
        copyButton.className = 'copy-button';
        copyButton.style.cssText = `
            float: right;
            background: #003300;
            color: #00ffff;
            border: 1px solid #00ffff;
            border-radius: 4px;
            padding: 4px 8px;
            font-family: 'Courier New', monospace;
            font-size: 0.8rem;
            cursor: pointer;
            margin-left: 5px;
            transition: all 0.2s ease;
        `;
        
        copyButton.addEventListener('click', () => {
            const text = snippet.textContent;
            navigator.clipboard.writeText(text).then(() => {
                const originalText = copyButton.textContent;
                copyButton.textContent = 'Copied!';
                setTimeout(() => {
                    copyButton.textContent = originalText;
                }, 2000);
            });
        });
        
        snippet.parentNode.style.position = 'relative';
        snippet.parentNode.appendChild(copyButton);
    });
});