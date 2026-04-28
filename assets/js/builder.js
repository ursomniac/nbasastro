document.addEventListener('DOMContentLoaded', function() {
    const btn = document.getElementById('generate-btn');
    if (!btn) return;

    btn.onclick = function() {
        try {
            const getV = (id) => document.getElementById(id)?.value.trim() || "";

            // 1. START YAML
            let yaml = "---\n";
            yaml += `title: "${getV('r-title') || 'Untitled'}"\n`;
            yaml += `date: "${getV('r-date')}"\n`;
            yaml += `byline: "${getV('r-byline')}"\n`;

            const authVal = getV('r-authors');
            const auths = authVal ? authVal.split(',').map(s => `"${s.trim()}"`) : ['"Member"'];
            yaml += `authors: [${auths.join(', ')}]\n`;

            if (getV('o-series')) yaml += `series: ["${getV('o-series')}"]\n`;
            const tagsVal = getV('o-tags');
            if (tagsVal) {
                const tags = tagsVal.split(',').map(s => `"${s.trim()}"`);
                yaml += `tags: [${tags.join(', ')}]\n`;
            }
            
            const know = Array.from(document.querySelectorAll('.tax-know:checked')).map(c => `"${c.value}"`);
            if (know.length) yaml += `knowledgetopics: [${know.join(', ')}]\n`;

            // 2. SOLAR SYSTEM (Taxonomy + object_sections)
            let ssBlock = "";
            const taxSolar = [];
            document.querySelectorAll('.val-ss').forEach(input => {
                if (input.parentElement.style.display === 'block') {
                    taxSolar.push(`"${input.dataset.cat}"`);
                    if (input.value) {
                        const items = input.value.split(',').map(s => `"${s.trim()}"`);
                        ssBlock += `  ${input.dataset.cat}: [${items.join(', ')}]\n`;
                    }
                }
            });
            if (taxSolar.length) yaml += `solarsystem: [${taxSolar.join(', ')}]\n`;

            // 3. DSO CATALOGS (object_sections)
            let catBlock = "";
            document.querySelectorAll('.val-cat').forEach(input => {
                if (input.value && input.parentElement.style.display === 'block') {
                    const items = input.value.split(',').map(s => `"${s.trim()}"`);
                    catBlock += `  ${input.dataset.cat}: [${items.join(', ')}]\n`;
                }
            });

            // Combine SS and Catalogs into object_sections
            if (ssBlock || catBlock) yaml += `object_sections:\n${ssBlock}${catBlock}`;

            // 4. STAR DATA
            let starData = "";
            const taxStar = [];
            document.querySelectorAll('.val-star').forEach(input => {
                if (input.parentElement.style.display === 'block') {
                    taxStar.push(`"${input.dataset.cat}"`);
                    if (input.value) {
                        const items = input.value.split(',').map(s => `"${s.trim()}"`);
                        starData += `  ${input.dataset.cat}: [${items.join(', ')}]\n`;
                    }
                }
            });
            if (taxStar.length) yaml += `stargroups: [${taxStar.join(', ')}]\n`;
            if (starData) yaml += `stardata:\n${starData}`;

            // 5. OBJECT INFO (SPECS TABLE)
            let specBlock = "";
            let hasSpecs = false;
            document.querySelectorAll('#specs-list .check-row-wrapper').forEach(row => {
                const l = row.querySelector('.spec-label').value.trim();
                const v = row.querySelector('.spec-value').value.trim();
                if (l && v) {
                    hasSpecs = true;
                    specBlock += `  ${l.toLowerCase().replace(/ /g, '_')}: "${v}"\n`;
                }
            });
            if (specBlock) yaml += `object_info:\n${specBlock}`;

            // 6. CONTENT SECTION
            let body = "\n---\n\n## Introduction\n\n";
            if (hasSpecs) body += "{{< object-specs >}}\n\n";
            body += "Write content here...\n\n";

            if (document.getElementById('snip-img-align')?.checked) {
                body += `{{< nbas-image src="file.png" align="right" width="400" >}}\n\n`;
            }
            if (document.getElementById('snip-img-center')?.checked) {
                body += `{{< nbas-image src="file.png" >}}\n\n`;
            }
            if (document.getElementById('snip-img-full')?.checked) {
                body += `{{< nbas-image src="file.png" fullwidth="true" >}}\n\n`;
            }
            if (document.getElementById('snip-gal-grid')?.checked) {
                body += `{{< nbas-gallery type="grid" >}}\nmyimage1.png | Caption text here | Image Credit Name\n{{< /nbas-gallery >}}\n\n`;
            }
            if (document.getElementById('snip-gal-caro')?.checked) {
                body += `{{< nbas-gallery type="carousel" >}}\nmyimage1.png | Caption text here | Image Credit Name\n{{< /nbas-gallery >}}\n\n`;
            }
            if (document.getElementById('snip-video')?.checked) {
                body += `{{< nbas-video id="VIDEO_ID" title="Video Title" >}}\n\n`;
            }

            const blob = new Blob([yaml + body], { type: 'text/markdown' });
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'index.md';
            a.click();

        } catch (err) {
            console.error("Builder Error:", err);
            alert("Check console (F12) for error details.");
        }
    };
});

