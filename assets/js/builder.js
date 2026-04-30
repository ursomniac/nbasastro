document.addEventListener('DOMContentLoaded', function() {
    const btn = document.getElementById('generate-btn');
    if (!btn) return;

    btn.onclick = function() {
        try {
            const getV = (id) => document.getElementById(id)?.value.trim() || "";
            
            // 1. GLOBAL METADATA
            let yaml = "---\n";
            yaml += `title: "${getV('r-title') || 'Untitled'}"\n`;
            yaml += `date: "${getV('r-date')}"\n`;
            yaml += `byline: "${getV('r-byline')}"\n`;

            const authVal = getV('r-authors');
            const auths = authVal ? authVal.split(',').map(s => `"${s.trim()}"`) : ['"NBAS Staff"'];
            yaml += `authors: [${auths.join(', ')}]\n`;

            if (getV('o-series')) yaml += `series: ["${getV('o-series')}"]\n`;

            const tagsVal = getV('o-tags');
            if (tagsVal) {
                const tags = tagsVal.split(',').map(s => `"${s.trim()}"`);
                yaml += `tags: [${tags.join(', ')}]\n`;
            }

            const know = Array.from(document.querySelectorAll('.tax-know:checked')).map(c => `"${c.value}"`);
            if (know.length) yaml += `knowledgetopics: [${know.join(', ')}]\n`;

            // 2. FLATTENED ASTRONOMY TAXONOMIES
            // Map form categories to Hugo keys
            const mapping = {
                // Solar System
                "planets": "sso_planets", "meteors": "sso_meteors", 
                "comets": "sso_comets", "asteroids": "sso_asteroids",
                // DSO
                "messier": "dso_messier", "caldwell": "dso_caldwell", 
                "ngc": "dso_ngc", "other": "dso_other",
                // Stars
                "variable": "stars_variable", "nearby": "stars_nearby", 
                "bright": "stars_bright", "multiple": "stars_multiple", 
                "exotic": "stars_exotic"
            };

            // Process all inputs that have data-cat
	    // Replace the previous data-cat processing block with this:
	    document.querySelectorAll('.val-astro').forEach(input => {
    	   	const category = input.dataset.cat;
    		const hugoKey = mapping[category];
    
		// Only include if the field has values
		if (hugoKey && input.value) {
		   const items = input.value.split(',').map(s => `"${s.trim()}"`);
	           yaml += `${hugoKey}: [${items.join(', ')}]\n`;
		}
	    });

            // 3. OBJECT SPECS (TABLE)
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

            // 4. CONTENT SECTION
            let body = "\n---\n\n## Introduction\n\n";
            if (hasSpecs) body += "{{< object-specs >}}\n\n";
            body += "Write content here...\n\n";

            // Shortcodes
            if (document.getElementById('snip-img-align')?.checked) body += `{{< nbas-image src="file.png" align="right" width="400" >}}\n\n`;
            if (document.getElementById('snip-img-center')?.checked) body += `{{< nbas-image src="file.png" >}}\n\n`;
            if (document.getElementById('snip-img-full')?.checked) body += `{{< nbas-image src="file.png" fullwidth="true" >}}\n\n`;
            if (document.getElementById('snip-gal-grid')?.checked) body += `{{< nbas-gallery type="grid" >}}\nimage1.png | Caption | Credit\n{{< /nbas-gallery >}}\n\n`;
            if (document.getElementById('snip-gal-caro')?.checked) body += `{{< nbas-gallery type="carousel" >}}\nimage1.png | Caption | Credit\n{{< /nbas-gallery >}}\n\n`;
            if (document.getElementById('snip-video')?.checked) body += `{{< nbas-video id="ID" title="Title" >}}\n\n`;

            // DOWNLOAD
            const blob = new Blob([yaml + body], { type: 'text/markdown' });
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'index.md';
            a.click();

        } catch (err) {
            console.error("Builder Error:", err);
            alert("Builder Error: " + err.message);
        }
    };
});

