const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

// Replace <img without loading= with <img loading="lazy"
const newContent = content.replace(/<img(?![^>]*\bloading=)([^>]*)>/gi, '<img loading="lazy"$1>');

fs.writeFileSync('index.html', newContent, 'utf8');

console.log('Patch applied.');
