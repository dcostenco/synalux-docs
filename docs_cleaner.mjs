import fs from 'fs';
import path from 'path';

const DOCS_DIR = path.join(process.cwd(), 'docs_source_en');

function processMarkdown(content) {
    let lines = content.split('\n');
    let result = [];
    let i = 0;

    while (i < lines.length) {
        let line = lines[i];

        // Check if we are already inside a details block (simple check)
        if (line.includes('<details>')) {
            result.push(line);
            i++;
            let nestedCount = 1;
            while (i < lines.length && nestedCount > 0) {
                if (lines[i].includes('<details>')) nestedCount++;
                if (lines[i].includes('</details>')) nestedCount--;
                result.push(lines[i]);
                i++;
            }
            continue;
        }

        let isMarkdownImage = line.trim().startsWith('![');
        let isHtmlImage = line.trim().startsWith('<img');

        if (isMarkdownImage || isHtmlImage) {
            result.push('<details>');
            result.push('<summary>View Interface / Diagram</summary>\n');
            result.push(line);
            i++;

            // Look ahead for captions
            while (i < lines.length) {
                let nextLine = lines[i].trim();
                if (nextLine === '' || nextLine.startsWith('#') || nextLine.startsWith('![') || nextLine.startsWith('<img') || nextLine.startsWith('```')) {
                    break;
                }
                // If it looks like a caption (starts with * and ends with *)
                if (nextLine.startsWith('*') && nextLine.endsWith('*') && !nextLine.includes('**')) {
                    result.push(lines[i]);
                    i++;
                } else {
                    break;
                }
            }
            result.push('\n</details>');
            continue;
        }

        // Check for code block
        if (line.trim().startsWith('```')) {
            result.push('<details>');
            result.push('<summary>Technical Documentation / Specifications</summary>\n');
            result.push(line);
            i++;
            while (i < lines.length && !lines[i].trim().startsWith('```')) {
                result.push(lines[i]);
                i++;
            }
            if (i < lines.length) {
                result.push(lines[i]);
                i++;
            }
            result.push('\n</details>');
            continue;
        }

        result.push(line);
        i++;
    }

    return result.join('\n');
}

const files = fs.readdirSync(DOCS_DIR).filter(file => file.endsWith('.md'));

let processedCount = 0;
for (const file of files) {
    const filePath = path.join(DOCS_DIR, file);
    const content = fs.readFileSync(filePath, 'utf-8');

    if (!content.includes('![') && !content.includes('<img') && !content.includes('```')) {
        continue;
    }

    const processed = processMarkdown(content);
    if (processed !== content) {
        fs.writeFileSync(filePath, processed, 'utf-8');
        processedCount++;
        console.log(`Processed: ${file}`);
    }
}

console.log(`\nComplete. Modified ${processedCount} files.`);
