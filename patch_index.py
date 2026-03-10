import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert the modal
modal_html = """
            <div id="shortmovieGridModal" class="modal fixed inset-0 z-[90] flex items-center justify-center bg-black/95 px-4">
                <div class="modal-content relative bg-dark-900 border border-dark-600 rounded-lg max-w-6xl w-full max-h-[90vh] flex flex-col overflow-hidden shadow-[0_0_40px_rgba(0,240,255,0.05)]">

                    <div class="flex justify-between items-center p-6 border-b border-dark-700 bg-dark-800/80 backdrop-blur sticky top-0 z-20">
                        <div>
                            <h3 class="text-2xl font-bold font-display text-white">SHORTMOVIE <span class="text-accent">COLLECTION</span></h3>
                            <p class="text-xs text-gray-500 tracking-widest uppercase mt-1">Short Films & Teasers</p>
                        </div>
                        <button id="closeShortmovieGridModal" class="w-10 h-10 rounded-full bg-dark-800 border border-dark-600 text-gray-400 hover:text-white hover:border-accent transition-all duration-300 flex items-center justify-center"><i class="fas fa-times text-lg"></i></button>
                    </div>

                    <div class="flex-grow overflow-y-auto p-6 scroll-smooth">
                        <div class="grid grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-3 md:gap-6">

"""

projects = [
    {
        "title": "INDRAMAYU – FORGOTTEN LAND",
        "desc": "Cinematic exploration of the forgotten lands of Indramayu.",
        "id": "-xeDt_6XxJg",
        "role": "Lead Editor",
        "year": "2024"
    },
    {
        "title": "PROKLAMASI",
        "desc": "Short film drama sejarah tentang peristiwa Rengasdengklok.",
        "id": "rfRnIAlNcvg",
        "role": "Lead Editor",
        "year": "2023"
    },
    {
        "title": "JUNI - SHORTMOVIE",
        "desc": "Proyek film pendek drama emosional.",
        "id": "WX4Ju2Ja6lA",
        "role": "Editor & Colorist",
        "year": "2023"
    },
    {
        "title": "SUWUNG - TRAILER",
        "desc": "Trailer film pendek bergenre horor misterius.",
        "id": "4iOvfP2j-qo",
        "role": "Film, Editing, Acting, VFX & CGI",
        "year": "2026"
    },
    {
        "title": "TEASER MOVIE EVENT INDRAMAYU",
        "desc": "Teaser sinematik untuk event film di Indramayu.",
        "id": "Yk5eKsjo014",
        "role": "Film, Editing, Acting, VFX & CGI",
        "year": "2026"
    },
    {
        "title": "PEKA - MOVIE",
        "desc": "Proyek penyuntingan film PEKA.",
        "id": "Po7iPDfMFa0",
        "role": "Lead Editor",
        "year": "2022"
    },
    {
        "title": "BULLYING - ILM",
        "desc": "Iklan Layanan Masyarakat edukatif sekolah untuk mencegah bullying.",
        "id": "1Avk8cpuxtw",
        "role": "Director & Editor",
        "year": "2023"
    },
    {
        "title": "CERMIN - HORROR",
        "desc": "Short film horor psikologis berfokus pada visual efek cermin.",
        "id": "-WHtnDVKKu4",
        "role": "VFX & Editor",
        "year": "2024"
    },
    {
        "title": "HUTAN PEMBUNUH",
        "desc": "Film horor suspense dengan color grading cinematic di hutan gelap.",
        "id": "Mx7UcSYrf_g",
        "role": "Compositor",
        "year": "2023"
    },
    {
        "title": "PAHLAWAN LANGIT",
        "desc": "Proyek VFX action bertema pahlawan super lokal Indonesia.",
        "id": "eiy-AzVXrpE",
        "role": "VFX Generalist",
        "year": "2022"
    }
]

for p in projects:
    modal_html += f"""                            <div class="card-glass rounded-lg overflow-hidden group flex flex-col">
                                <div class="relative aspect-video bg-dark-900 overflow-hidden">
                                    <img src="https://img.youtube.com/vi/{p['id']}/maxresdefault.jpg"
                                        onerror="this.onerror=null; this.src='https://img.youtube.com/vi/{p['id']}/hqdefault.jpg'"
                                        alt="{p['title']}" loading="lazy"
                                        class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105">
                                    <div class="absolute inset-0 bg-black/70 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center gap-4 backdrop-blur-[2px]">
                                        <button onclick="openProject('youtube', '{p['title'].replace("'", "\\'")}', '{p['desc'].replace("'", "\\'")}', '{p['id']}', '{p['role'].replace("'", "\\'")}', '{p['year']}')" class="w-12 h-12 rounded-full bg-accent/20 border border-accent/50 hover:bg-accent hover:text-dark-900 text-white flex items-center justify-center transition-all duration-300 transform scale-75 group-hover:scale-100" title="Play Video">
                                            <i class="fas fa-play ml-1"></i>
                                        </button>
                                        <a href="https://youtu.be/{p['id']}" target="_blank" class="w-12 h-12 rounded-full bg-white/10 border border-white/20 hover:bg-white hover:text-dark-900 text-white flex items-center justify-center transition-all duration-300 transform scale-75 group-hover:scale-100 delay-75" title="Open External Link">
                                            <i class="fas fa-external-link-alt"></i>
                                        </a>
                                    </div>
                                </div>
                                <div class="p-4 flex flex-col flex-grow">
                                    <h4 class="text-white font-bold text-base font-display mb-1 truncate">{p['title']}</h4>
                                    <p class="text-xs text-gray-400 line-clamp-2">{p['desc']}</p>
                                </div>
                            </div>
"""

modal_html += """                        </div>
                    </div>
                </div>
            </div>\n"""

# Replace in content (before <div class="grid grid-cols-2 lg:grid-cols-3 gap-3 md:gap-6" id="portfolioGrid">)
target_grid = '<div class="grid grid-cols-2 lg:grid-cols-3 gap-3 md:gap-6" id="portfolioGrid">'
if target_grid in content:
    content = content.replace(target_grid, modal_html + '\n            ' + target_grid)
else:
    print("Error: Could not find target Grid")

# 2. Insert the card
card_html = """
                <div class="card-glass rounded-lg overflow-hidden group portfolio-item reveal"
                    data-category="film editing acting vfx" data-title="SHORTMOVIE COLLECTION">
                    <div class="relative aspect-video bg-dark-900 overflow-hidden cursor-pointer"
                        onclick="openShortmovieGridModal()">
                        <img src="https://img.youtube.com/vi/-xeDt_6XxJg/maxresdefault.jpg"
                            onerror="this.onerror=null; this.src='https://img.youtube.com/vi/-xeDt_6XxJg/hqdefault.jpg'"
                            alt="SHORTMOVIE Collection" loading="lazy"
                            class="w-full h-full object-cover opacity-70 group-hover:scale-105 transition duration-700">
                        <div
                            class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center gap-3 backdrop-blur-[2px]">
                            <button
                                class="w-12 h-12 rounded-full bg-accent/20 border border-accent/50 hover:bg-accent hover:text-dark-900 text-white flex items-center justify-center transition-all duration-300 transform scale-75 group-hover:scale-100 shadow-[0_0_15px_rgba(0,240,255,0.3)]"
                                title="Open Shortmovie Gallery">
                                <i class="fas fa-layer-group text-xl"></i>
                            </button>
                        </div>
                        <div
                            class="absolute top-3 right-3 px-2 py-1 bg-dark-900/80 backdrop-blur rounded text-[10px] font-bold tracking-wider text-white uppercase border border-dark-600">
                            COLLECTION
                        </div>
                    </div>
                    <div class="p-5">
                        <div class="flex justify-between items-start mb-2">
                            <h3 class="text-white font-bold text-lg font-display truncate">SHORTMOVIE COLLECTION</h3>
                            <span class="text-[10px] uppercase tracking-wider text-accent font-medium mt-1">FILM</span>
                        </div>
                        <p class="text-sm text-gray-400 mb-4 line-clamp-2">Kumpulan proyek film pendek, teaser, trailer, dan karya sinematik yang saya kerjakan sebagai editor, VFX artist, dan storyteller.</p>
                        <div class="flex gap-3 text-sm text-gray-500 border-t border-dark-700 pt-3">
                            <i class="fa-solid fa-film hover:text-white transition-colors" title="Film"></i>
                            <i class="fa-solid fa-scissors hover:text-white transition-colors" title="Editing"></i>
                            <i class="fa-solid fa-clapperboard hover:text-white transition-colors" title="Storytelling"></i>
                        </div>
                    </div>
                </div>
"""

# Insert after Commercial Edit card.
# The commercial card ends right before <div class="card-glass ... data-title="INDRAMAYU – THE FORGOTTEN LAND">
target_insert = '''                <div class="card-glass rounded-lg overflow-hidden group portfolio-item reveal"
                    data-category="editing vfx" data-title="INDRAMAYU – THE FORGOTTEN LAND">'''
if target_insert in content:
    content = content.replace(target_insert, card_html + '\n' + target_insert)
else:
    print("Error: Could not find Indramayu target")


# 3. Add JS
js_logic = """
        // 7b. Logic SHORTMOVIE Portfolio Grid Modal
        const shortmovieGridModal = document.getElementById('shortmovieGridModal');
        const closeShortmovieGridModal = document.getElementById('closeShortmovieGridModal');

        window.openShortmovieGridModal = function () {
            if (shortmovieGridModal) {
                shortmovieGridModal.classList.add('active');
                document.body.style.overflow = 'hidden';
            }
        }

        if (closeShortmovieGridModal) {
            closeShortmovieGridModal.addEventListener('click', () => {
                shortmovieGridModal.classList.remove('active');
                const pModal = document.getElementById('projectModal');
                if (!pModal || !pModal.classList.contains('active')) {
                    document.body.style.overflow = 'auto';
                }
            });
        }

        window.addEventListener('click', (e) => {
            if (e.target === shortmovieGridModal) {
                shortmovieGridModal.classList.remove('active');
                const pModal = document.getElementById('projectModal');
                if (!pModal || !pModal.classList.contains('active')) {
                    document.body.style.overflow = 'auto';
                }
            }
        });
"""

# Update CloseProjModal
# It originally has:
#                 const vfxModalActive = document.getElementById('vfxGridModal') && document.getElementById('vfxGridModal').classList.contains('active');
#                 const threeDModalActive = document.getElementById('threeDGridModal') && document.getElementById('threeDGridModal').classList.contains('active');
#                 if (!vfxModalActive && !threeDModalActive) {
#                     document.body.style.overflow = 'auto';
#                 }
old_js_check = "if (!vfxModalActive && !threeDModalActive) {"
new_js_check = "const shortmovieModalActive = document.getElementById('shortmovieGridModal') && document.getElementById('shortmovieGridModal').classList.contains('active');\n                if (!vfxModalActive && !threeDModalActive && !shortmovieModalActive) {"
if old_js_check in content:
    content = content.replace(old_js_check, new_js_check)
else:
    print("Error: Could not find js check target")

target_js_insert = "// ==========================================\n        // 8. 3D PORTFOLIO & ADVANCED VIEWER LOGIC"
if target_js_insert in content:
    content = content.replace(target_js_insert, js_logic + '\n        ' + target_js_insert)
else:
    print("Error: Could not find js insert target")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied.")
