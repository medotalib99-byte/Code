<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mohamed Mahmoud Talib, MSc | Public Health Informatics Portfolio</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#f0f7ff',
                            100: '#e0effe',
                            500: '#0284c7',
                            600: '#0369a1',
                            700: '#075985',
                            800: '#0c4a6e',
                            900: '#0a3651',
                        },
                        emerald: {
                            500: '#10b981',
                            600: '#059669',
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Leaflet JS & CSS for Geospatial Mapping -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <!-- Inter Font -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        .glass-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(226, 232, 240, 0.8);
        }
        #leaflet-map {
            height: 480px;
            width: 100%;
            border-radius: 0.75rem;
            z-index: 10;
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased selection:bg-brand-500 selection:text-white">

    <!-- NAVIGATION BAR -->
    <nav class="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-slate-200 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <div class="flex items-center gap-3">
                    <img src="Pic.jpg" onerror="this.src='https://placehold.co/100x100/0284c7/ffffff?text=MT'" alt="Mohamed Talib" class="w-10 h-10 rounded-full object-cover border-2 border-brand-600 shadow-sm">
                    <div>
                        <span class="font-bold text-slate-900 text-lg leading-tight block">Mohamed Talib, <span class="text-brand-600">MSc</span></span>
                        <span class="text-xs text-slate-500 block">Public Health Informatics Professional</span>
                    </div>
                </div>

                <!-- Desktop Nav Links -->
                <div class="hidden md:flex items-center space-x-1 lg:space-x-4 font-medium text-sm">
                    <a href="#home" class="px-3 py-2 rounded-lg text-slate-600 hover:text-brand-600 hover:bg-slate-100 transition">Home</a>
                    <a href="#about" class="px-3 py-2 rounded-lg text-slate-600 hover:text-brand-600 hover:bg-slate-100 transition">About Me</a>
                    <a href="#visualizations" class="px-3 py-2 rounded-lg text-slate-600 hover:text-brand-600 hover:bg-slate-100 transition"><i class="fa-solid font-chart-line text-brand-600 mr-1"></i> Interactive Work</a>
                    <a href="#services" class="px-3 py-2 rounded-lg text-slate-600 hover:text-brand-600 hover:bg-slate-100 transition">Services</a>
                    <a href="#reviews" class="px-3 py-2 rounded-lg text-slate-600 hover:text-brand-600 hover:bg-slate-100 transition">Reviews</a>
                    <a href="#contact" class="px-4 py-2 rounded-lg bg-brand-600 text-white hover:bg-brand-700 transition shadow-sm font-semibold">Contact Me</a>
                </div>

                <!-- Mobile Menu Button -->
                <button id="mobile-menu-btn" class="md:hidden p-2 rounded-lg text-slate-600 hover:bg-slate-100">
                    <i class="fa-solid fa-bars text-xl"></i>
                </button>
            </div>
        </div>

        <!-- Mobile Nav Menu -->
        <div id="mobile-menu" class="hidden md:hidden border-b border-slate-200 bg-white px-4 pt-2 pb-4 space-y-1">
            <a href="#home" class="block px-3 py-2 rounded-lg text-slate-700 hover:bg-slate-100">Home</a>
            <a href="#about" class="block px-3 py-2 rounded-lg text-slate-700 hover:bg-slate-100">About Me</a>
            <a href="#visualizations" class="block px-3 py-2 rounded-lg text-brand-600 font-semibold hover:bg-slate-100">Interactive Work</a>
            <a href="#services" class="block px-3 py-2 rounded-lg text-slate-700 hover:bg-slate-100">Services</a>
            <a href="#reviews" class="block px-3 py-2 rounded-lg text-slate-700 hover:bg-slate-100">Reviews</a>
            <a href="#contact" class="block px-3 py-2 rounded-lg bg-brand-600 text-white font-medium text-center">Contact Me</a>
        </div>
    </nav>

    <!-- HERO / HOME SECTION -->
    <section id="home" class="relative bg-gradient-to-b from-slate-900 via-brand-900 to-slate-900 text-white py-16 md:py-24 overflow-hidden">
        <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#38bdf8_1px,transparent_1px)] [background-size:16px_16px]"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
                
                <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
                    <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-brand-500/20 border border-brand-400/30 text-brand-300 text-xs sm:text-sm font-medium">
                        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                        Africa CDC / ZNPHI Informatics Fellow
                    </div>
                    <h1 class="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-extrabold tracking-tight leading-tight">
                        Mohamed Mahmoud <br><span class="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 to-emerald-400">Talib, MSc</span>
                    </h1>
                    <p class="text-base sm:text-lg text-slate-300 font-normal leading-relaxed max-w-2xl">
                        Specializing in <span class="text-white font-semibold">Epidemiology, Digital Health in Africa</span>, and <span class="text-white font-semibold">Artificial Intelligence & Data Science</span> to strengthen disease surveillance, outbreak evaluation, and epidemic forecasting across fragile contexts.
                    </p>

                    <!-- Contact Pills -->
                    <div class="flex flex-wrap gap-3 justify-center lg:justify-start text-xs sm:text-sm text-slate-300">
                        <div class="flex items-center gap-2 bg-slate-800/80 px-3 py-2 rounded-lg border border-slate-700">
                            <i class="fa-solid fa-location-dot text-brand-400"></i>
                            <span>Lusaka, Zambia</span>
                        </div>
                        <a href="mailto:medo.talib99@gmail.com" class="flex items-center gap-2 bg-slate-800/80 px-3 py-2 rounded-lg border border-slate-700 hover:border-brand-500 transition">
                            <i class="fa-solid fa-envelope text-brand-400"></i>
                            <span>medo.talib99@gmail.com</span>
                        </a>
                        <a href="https://wa.me/249912559111" target="_blank" class="flex items-center gap-2 bg-slate-800/80 px-3 py-2 rounded-lg border border-slate-700 hover:border-emerald-400 transition">
                            <i class="fa-brands fa-whatsapp text-emerald-400"></i>
                            <span>+249 912 559 111</span>
                        </a>
                    </div>

                    <!-- Call To Action Buttons -->
                    <div class="pt-4 flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
                        <a href="#visualizations" class="inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl bg-gradient-to-r from-brand-500 to-brand-600 text-white font-semibold shadow-lg shadow-brand-500/25 hover:from-brand-600 hover:to-brand-700 transition">
                            <i class="fa-solid fa-chart-pie"></i> Explore Interactive Dashboards
                        </a>
                        <a href="https://www.linkedin.com/in/mohamed-talib-664331158" target="_blank" class="inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-semibold border border-slate-700 transition">
                            <i class="fa-brands fa-linkedin text-sky-400"></i> LinkedIn Profile
                        </a>
                    </div>
                </div>

                <!-- Profile Photo Card -->
                <div class="lg:col-span-5 flex justify-center">
                    <div class="relative w-full max-w-sm">
                        <div class="absolute -inset-1 rounded-2xl bg-gradient-to-r from-brand-500 to-emerald-500 blur-lg opacity-40"></div>
                        <div class="relative bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-2xl">
                            <img src="Pic.jpg" onerror="this.src='https://placehold.co/600x600/0284c7/ffffff?text=Mohamed+Talib+MSc'" alt="Mohamed Talib Portrait" class="w-full h-80 sm:h-96 object-cover rounded-xl shadow-md">
                            <div class="mt-4 text-center">
                                <h3 class="font-bold text-lg text-white">Mohamed M. Talib</h3>
                                <p class="text-xs text-brand-300">Public Health Informatics & Research Specialist</p>
                                <div class="mt-3 flex justify-center gap-2">
                                    <span class="px-2.5 py-1 rounded bg-slate-800 text-[11px] text-slate-300 border border-slate-700">Epidemiology</span>
                                    <span class="px-2.5 py-1 rounded bg-slate-800 text-[11px] text-slate-300 border border-slate-700">AI & ML</span>
                                    <span class="px-2.5 py-1 rounded bg-slate-800 text-[11px] text-slate-300 border border-slate-700">M&E</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- KEY STATS STRIP -->
    <section class="bg-white border-y border-slate-200 py-8 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
                    <div class="text-3xl font-bold text-brand-600">7+ Years</div>
                    <div class="text-xs sm:text-sm text-slate-600 font-medium mt-1">Public Health Experience</div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
                    <div class="text-3xl font-bold text-emerald-600">20+</div>
                    <div class="text-xs sm:text-sm text-slate-600 font-medium mt-1">Research & M&E Projects</div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
                    <div class="text-3xl font-bold text-brand-600">3</div>
                    <div class="text-xs sm:text-sm text-slate-600 font-medium mt-1">Countries Impacted</div>
                </div>
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-100">
                    <div class="text-3xl font-bold text-indigo-600">100%</div>
                    <div class="text-xs sm:text-sm text-slate-600 font-medium mt-1">Rigour & Equity Focus</div>
                </div>
            </div>
        </div>
    </section>

    <!-- ABOUT ME SECTION -->
    <section id="about" class="py-16 md:py-24 bg-slate-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-xs font-bold uppercase tracking-wider text-brand-600 mb-2">Background & Expertise</h2>
                <p class="text-3xl font-bold text-slate-900">About Mohamed Talib</p>
                <p class="mt-3 text-slate-600 leading-relaxed">
                    Combining advanced data analytics, artificial intelligence, field epidemiology, and strategic partnership development to build resilient health systems in complex environments.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Academic Column -->
                <div class="bg-white p-8 rounded-2xl border border-slate-200 shadow-sm space-y-6">
                    <div class="flex items-center gap-3 border-b border-slate-100 pb-4">
                        <div class="w-10 h-10 rounded-lg bg-brand-50 text-brand-600 flex items-center justify-center font-bold text-lg">
                            <i class="fa-solid fa-graduation-cap"></i>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900">Academic Background</h3>
                    </div>

                    <ul class="space-y-4">
                        <li class="flex gap-4">
                            <div class="mt-1 w-2.5 h-2.5 rounded-full bg-brand-600 flex-shrink-0"></div>
                            <div>
                                <h4 class="font-bold text-slate-900">Doctor of Humanitarian Action & Development <span class="text-xs font-normal text-slate-500">(Candidate)</span></h4>
                                <p class="text-sm text-slate-600">Geneva Institute of Humanitarian & Development Studies</p>
                            </div>
                        </li>
                        <li class="flex gap-4">
                            <div class="mt-1 w-2.5 h-2.5 rounded-full bg-brand-600 flex-shrink-0"></div>
                            <div>
                                <h4 class="font-bold text-slate-900">MSc in Applied Data Science and Artificial Intelligence</h4>
                                <p class="text-sm text-slate-600">European Global Institute</p>
                            </div>
                        </li>
                        <li class="flex gap-4">
                            <div class="mt-1 w-2.5 h-2.5 rounded-full bg-brand-600 flex-shrink-0"></div>
                            <div>
                                <h4 class="font-bold text-slate-900">Master by Research in Public Health</h4>
                                <p class="text-sm text-slate-600">University of Bahri</p>
                            </div>
                        </li>
                        <li class="flex gap-4">
                            <div class="mt-1 w-2.5 h-2.5 rounded-full bg-brand-600 flex-shrink-0"></div>
                            <div>
                                <h4 class="font-bold text-slate-900">BSc in Public and Environmental Health</h4>
                                <p class="text-sm text-slate-600">University of Bahri</p>
                            </div>
                        </li>
                    </ul>
                </div>

                <!-- Technical Stack Column -->
                <div class="bg-white p-8 rounded-2xl border border-slate-200 shadow-sm space-y-6">
                    <div class="flex items-center gap-3 border-b border-slate-100 pb-4">
                        <div class="w-10 h-10 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center font-bold text-lg">
                            <i class="fa-solid fa-code"></i>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900">Technical & Analytical Stack</h3>
                    </div>

                    <div class="space-y-4">
                        <div>
                            <span class="text-xs font-bold text-slate-500 uppercase tracking-wider block mb-2">Data Science & Programming</span>
                            <div class="flex flex-wrap gap-2">
                                <span class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-800 text-sm font-medium">Python (Pandas, Scikit-Learn)</span>
                                <span class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-800 text-sm font-medium">R Programming</span>
                                <span class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-800 text-sm font-medium">SQL</span>
                                <span class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-800 text-sm font-medium">STATA & SPSS</span>
                            </div>
                        </div>

                        <div>
                            <span class="text-xs font-bold text-slate-500 uppercase tracking-wider block mb-2">GIS & Spatial Analysis</span>
                            <div class="flex flex-wrap gap-2">
                                <span class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-800 text-sm font-medium">QGIS & ArcGIS</span>
                                <span class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-800 text-sm font-medium">GeoPandas</span>
                                <span class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-800 text-sm font-medium">Leaflet Mapping</span>
                            </div>
                        </div>

                        <div>
                            <span class="text-xs font-bold text-slate-500 uppercase tracking-wider block mb-2">Digital Health Platforms</span>
                            <div class="flex flex-wrap gap-2">
                                <span class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-800 text-sm font-medium">DHIS2 System Admin</span>
                                <span class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-800 text-sm font-medium">KoboToolbox</span>
                                <span class="px-3 py-1.5 rounded-lg bg-slate-100 text-slate-800 text-sm font-medium">Power BI & Tableau</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- INTERACTIVE DATA WORK & VISUALIZATIONS SECTION -->
    <section id="visualizations" class="py-16 md:py-24 bg-white border-t border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-12">
                <span class="px-3 py-1 rounded-full bg-brand-100 text-brand-700 text-xs font-semibold uppercase tracking-wider">Live Visualizations</span>
                <h2 class="text-3xl font-extrabold text-slate-900 mt-3">Interactive Data Work & Outbreak Analytics</h2>
                <p class="mt-2 text-slate-600">Simulated live surveillance dashboards, risk prediction models, and outbreak curves based on actual field experience.</p>
            </div>

            <!-- Visualization Navigation Tabs -->
            <div class="flex flex-wrap justify-center gap-2 mb-10 border-b border-slate-200 pb-4">
                <button onclick="switchVizTab('epidemic-curve')" id="tab-btn-epidemic-curve" class="viz-tab-btn active px-4 py-2.5 rounded-xl font-medium text-sm transition bg-brand-600 text-white shadow-sm">
                    <i class="fa-solid fa-chart-area mr-1.5"></i> Outbreak Surveillance Curve
                </button>
                <button onclick="switchVizTab('risk-simulator')" id="tab-btn-risk-simulator" class="viz-tab-btn px-4 py-2.5 rounded-xl font-medium text-sm transition bg-slate-100 text-slate-600 hover:bg-slate-200">
                    <i class="fa-solid fa-sliders mr-1.5"></i> Predictive Risk Simulator (ML)
                </button>
                <button onclick="switchVizTab('spatial-map')" id="tab-btn-spatial-map" class="viz-tab-btn px-4 py-2.5 rounded-xl font-medium text-sm transition bg-slate-100 text-slate-600 hover:bg-slate-200">
                    <i class="fa-solid fa-map-location-dot mr-1.5"></i> Spatial Risk Map
                </button>
                <button onclick="switchVizTab('research-dashboard')" id="tab-btn-research-dashboard" class="viz-tab-btn px-4 py-2.5 rounded-xl font-medium text-sm transition bg-slate-100 text-slate-600 hover:bg-slate-200">
                    <i class="fa-solid fa-folder-tree mr-1.5"></i> Digital Health Project Dashboard
                </button>
            </div>

            <!-- TAB 1: OUTBREAK CURVE SURVEILLANCE -->
            <div id="viz-epidemic-curve" class="viz-content space-y-6">
                <div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 shadow-sm">
                    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
                        <div>
                            <h3 class="text-xl font-bold text-slate-900">Cholera & Epidemic Outbreak Surveillance Curve</h3>
                            <p class="text-xs sm:text-sm text-slate-500">Weekly Epidemiological Case Counts by District & Intervention Timeline</p>
                        </div>
                        <!-- Controls -->
                        <div class="flex flex-wrap gap-3">
                            <select id="districtFilter" onchange="updateEpidemicChart()" class="bg-white border border-slate-300 text-slate-700 text-sm rounded-lg p-2 focus:ring-brand-500 focus:border-brand-500">
                                <option value="all">All Locations (Combined)</option>
                                <option value="gadarif">Gadarif State (Sudan Outbreak)</option>
                                <option value="chibombo">Chibombo / Kandindima (Zambia)</option>
                            </select>
                            <button onclick="toggleInterventionLine()" class="px-3 py-2 bg-slate-800 text-white text-xs font-semibold rounded-lg hover:bg-slate-700">
                                Toggle Intervention Markers
                            </button>
                        </div>
                    </div>

                    <!-- Chart Container -->
                    <div class="relative h-80 sm:h-96 w-full">
                        <canvas id="outbreakChart"></canvas>
                    </div>

                    <div class="mt-4 grid grid-cols-1 sm:grid-cols-3 gap-4 pt-4 border-t border-slate-200 text-center">
                        <div class="p-3 bg-white rounded-lg border border-slate-100">
                            <span class="text-xs text-slate-500 block">Peak Epidemiological Week</span>
                            <span class="text-lg font-bold text-brand-600">Week 8 (184 Cases)</span>
                        </div>
                        <div class="p-3 bg-white rounded-lg border border-slate-100">
                            <span class="text-xs text-slate-500 block">Post-Intervention Decline</span>
                            <span class="text-lg font-bold text-emerald-600">- 74.2%</span>
                        </div>
                        <div class="p-3 bg-white rounded-lg border border-slate-100">
                            <span class="text-xs text-slate-500 block">Active Surveillance Sites</span>
                            <span class="text-lg font-bold text-slate-800">14 Reporting Hubs</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 2: PREDICTIVE RISK SIMULATOR (ML) -->
            <div id="viz-risk-simulator" class="viz-content hidden space-y-6">
                <div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 shadow-sm">
                    <div class="mb-6">
                        <h3 class="text-xl font-bold text-slate-900">Machine Learning Epidemic Risk Score Calculator</h3>
                        <p class="text-sm text-slate-600">Simulate cholera & waterborne outbreak risk scores based on environmental and infrastructure variables.</p>
                    </div>

                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                        <!-- Sliders Column -->
                        <div class="lg:col-span-7 space-y-5 bg-white p-6 rounded-xl border border-slate-200">
                            
                            <div>
                                <div class="flex justify-between text-sm font-semibold mb-1">
                                    <label for="sliderRainfall" class="text-slate-700">Monthly Rainfall Index (mm)</label>
                                    <span id="valRainfall" class="text-brand-600">180 mm</span>
                                </div>
                                <input type="range" id="sliderRainfall" min="10" max="400" value="180" oninput="calculateRisk()" class="w-full accent-brand-600">
                            </div>

                            <div>
                                <div class="flex justify-between text-sm font-semibold mb-1">
                                    <label for="sliderSanitation" class="text-slate-700">Safe Sanitation Access (%)</label>
                                    <span id="valSanitation" class="text-brand-600">35 %</span>
                                </div>
                                <input type="range" id="sliderSanitation" min="5" max="100" value="35" oninput="calculateRisk()" class="w-full accent-brand-600">
                            </div>

                            <div>
                                <div class="flex justify-between text-sm font-semibold mb-1">
                                    <label for="sliderDensity" class="text-slate-700">Population Density (per sq km)</label>
                                    <span id="valDensity" class="text-brand-600">1,200</span>
                                </div>
                                <input type="range" id="sliderDensity" min="100" max="5000" value="1200" step="100" oninput="calculateRisk()" class="w-full accent-brand-600">
                            </div>

                            <div>
                                <div class="flex justify-between text-sm font-semibold mb-1">
                                    <label for="sliderWaterQuality" class="text-slate-700">Water Source Safety Score (0-100)</label>
                                    <span id="valWaterQuality" class="text-brand-600">45</span>
                                </div>
                                <input type="range" id="sliderWaterQuality" min="0" max="100" value="45" oninput="calculateRisk()" class="w-full accent-brand-600">
                            </div>

                        </div>

                        <!-- Risk Meter Output Column -->
                        <div class="lg:col-span-5 bg-white p-6 rounded-xl border border-slate-200 text-center space-y-4">
                            <span class="text-xs font-bold text-slate-400 uppercase tracking-wider block">Calculated Outbreak Risk Index</span>
                            
                            <div class="relative inline-flex items-center justify-center">
                                <div id="riskBadgeColor" class="w-36 h-36 rounded-full border-8 border-red-500 flex flex-col items-center justify-center shadow-inner transition-colors duration-300">
                                    <span id="riskScoreText" class="text-4xl font-extrabold text-slate-900">76</span>
                                    <span class="text-xs text-slate-500 font-semibold uppercase">out of 100</span>
                                </div>
                            </div>

                            <div id="riskLevelBox" class="p-3 rounded-lg bg-red-100 text-red-800 font-bold text-sm">
                                High Risk Level Detected
                            </div>

                            <p id="riskRecommendation" class="text-xs text-slate-600 text-left bg-slate-50 p-3 rounded-lg border border-slate-200">
                                Recommended Action: Immediate dispatch of oral cholera vaccines (OCV), deployment of mobile water testing kits, and rapid community engagement.
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TAB 3: SPATIAL RISK MAP -->
            <div id="viz-spatial-map" class="viz-content hidden space-y-4">
                <div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 shadow-sm">
                    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4">
                        <div>
                            <h3 class="text-xl font-bold text-slate-900">Geospatial Disease Surveillance & Focus Zones</h3>
                            <p class="text-sm text-slate-600">Interactive map highlighting key field locations, surveillance hubs, and outbreak risk zones in East/Central Africa.</p>
                        </div>
                        <div class="flex gap-2">
                            <button onclick="focusMap([14.0323, 35.3854], 8)" class="px-3 py-1.5 bg-white border border-slate-300 text-xs font-semibold rounded-lg hover:bg-slate-100">Focus Gadarif (Sudan)</button>
                            <button onclick="focusMap([-15.4167, 28.2833], 8)" class="px-3 py-1.5 bg-white border border-slate-300 text-xs font-semibold rounded-lg hover:bg-slate-100">Focus Lusaka & Chibombo (Zambia)</button>
                        </div>
                    </div>

                    <!-- Leaflet Container -->
                    <div id="leaflet-map" class="shadow-inner border border-slate-300"></div>
                </div>
            </div>

            <!-- TAB 4: RESEARCH PROJECT DASHBOARD -->
            <div id="viz-research-dashboard" class="viz-content hidden space-y-6">
                <div class="bg-slate-50 p-6 rounded-2xl border border-slate-200 shadow-sm">
                    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
                        <div>
                            <h3 class="text-xl font-bold text-slate-900">Digital Health & NTD Surveillance Impact Dashboard</h3>
                            <p class="text-sm text-slate-600">Selected research evaluations, system implementations, and public health consultations.</p>
                        </div>

                        <!-- Filter Buttons -->
                        <div class="flex flex-wrap gap-2">
                            <button onclick="filterProjects('all')" class="proj-filter-btn active text-xs font-semibold px-3 py-2 rounded-lg bg-brand-600 text-white">All Projects</button>
                            <button onclick="filterProjects('sam')" class="proj-filter-btn text-xs font-semibold px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-700 hover:bg-slate-100">Severe Acute Malnutrition (SAM)</button>
                            <button onclick="filterProjects('ntd')" class="proj-filter-btn text-xs font-semibold px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-700 hover:bg-slate-100">NTD Evaluation</button>
                            <button onclick="filterProjects('digital')" class="proj-filter-btn text-xs font-semibold px-3 py-2 rounded-lg bg-white border border-slate-300 text-slate-700 hover:bg-slate-100">Digital Surveillance</button>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6" id="projectsGrid">
                        
                        <!-- Card 1 -->
                        <div class="project-card bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-3" data-category="sam">
                            <div class="flex justify-between items-start">
                                <span class="px-2.5 py-1 rounded-full bg-amber-100 text-amber-800 text-xs font-bold">Nutrition / SAM</span>
                                <span class="text-xs text-slate-400">Published / Completed</span>
                            </div>
                            <h4 class="font-bold text-slate-900 leading-snug">Severe Acute Malnutrition (SAM) Program Evaluation</h4>
                            <p class="text-xs text-slate-600 leading-relaxed">Assessing treatment outcomes, relapse rates, and spatial distribution of SAM among pediatric populations in conflict-affected regions.</p>
                            <div class="pt-3 border-t border-slate-100 flex items-center justify-between text-xs font-medium text-brand-600">
                                <span>Statistical Tools: STATA / R</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </div>
                        </div>

                        <!-- Card 2 -->
                        <div class="project-card bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-3" data-category="digital">
                            <div class="flex justify-between items-start">
                                <span class="px-2.5 py-1 rounded-full bg-sky-100 text-sky-800 text-xs font-bold">Digital Health</span>
                                <span class="text-xs text-slate-400">Africa CDC</span>
                            </div>
                            <h4 class="font-bold text-slate-900 leading-snug">Integrated Disease Surveillance & Response (IDSR / DHIS2)</h4>
                            <p class="text-xs text-slate-600 leading-relaxed">Optimizing real-time digital reporting workflows and outbreak alert systems for national public health institutes.</p>
                            <div class="pt-3 border-t border-slate-100 flex items-center justify-between text-xs font-medium text-brand-600">
                                <span>Platform: DHIS2 / Python</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </div>
                        </div>

                        <!-- Card 3 -->
                        <div class="project-card bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-3" data-category="ntd">
                            <div class="flex justify-between items-start">
                                <span class="px-2.5 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold">NTD Systems</span>
                                <span class="text-xs text-slate-400">Surveillance</span>
                            </div>
                            <h4 class="font-bold text-slate-900 leading-snug">Neglected Tropical Diseases (NTD) Surveillance Evaluation</h4>
                            <p class="text-xs text-slate-600 leading-relaxed">Mapping endemicity of schistosomiasis and STH; evaluating mass drug administration (MDA) coverage indicators.</p>
                            <div class="pt-3 border-t border-slate-100 flex items-center justify-between text-xs font-medium text-brand-600">
                                <span>GIS Mapping & Analytics</span>
                                <i class="fa-solid fa-arrow-right"></i>
                            </div>
                        </div>

                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- SERVICES OFFERED SECTION -->
    <section id="services" class="py-16 md:py-24 bg-slate-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-xs font-bold uppercase tracking-wider text-brand-600 mb-2">Professional Services</h2>
                <p class="text-3xl font-bold text-slate-900">Tailored Expertise for Students & Organizations</p>
                <p class="mt-3 text-slate-600">Bridging academic research rigour with institutional monitoring, evaluation, and grant writing.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Services for Students -->
                <div class="bg-white p-8 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition">
                    <div class="w-12 h-12 rounded-xl bg-brand-50 text-brand-600 flex items-center justify-center font-bold text-xl mb-6">
                        <i class="fa-solid fa-user-graduate"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-slate-900 mb-3">Services for Students (PhD / MSc / BSc)</h3>
                    <p class="text-slate-600 text-sm mb-6 leading-relaxed">Comprehensive research mentorship and biostatistical guidance to help postgraduate students achieve academic publication.</p>
                    
                    <ul class="space-y-3 text-sm text-slate-700">
                        <li class="flex items-start gap-3">
                            <i class="fa-solid fa-circle-check text-emerald-500 mt-1"></i>
                            <span><strong>Proposal & Protocol Design:</strong> Conceptual frameworks, sample size calculations, and methodology.</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fa-solid fa-circle-check text-emerald-500 mt-1"></i>
                            <span><strong>Biostatistics & Data Analysis:</strong> Advanced modeling using R, Python, STATA, and SPSS.</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fa-solid fa-circle-check text-emerald-500 mt-1"></i>
                            <span><strong>Geospatial Spatial Mapping:</strong> High-resolution maps for thesis publications.</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fa-solid fa-circle-check text-emerald-500 mt-1"></i>
                            <span><strong>Scientific Writing & Publishing:</strong> Manuscript drafting and peer-review response support.</span>
                        </li>
                    </ul>

                    <div class="mt-8 pt-6 border-t border-slate-100">
                        <a href="#contact" class="inline-flex items-center text-sm font-semibold text-brand-600 hover:text-brand-700">
                            Inquire for Student Mentorship <i class="fa-solid fa-arrow-right ml-2"></i>
                        </a>
                    </div>
                </div>

                <!-- Services for Organizations -->
                <div class="bg-white p-8 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition">
                    <div class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center font-bold text-xl mb-6">
                        <i class="fa-solid fa-building-shield"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-slate-900 mb-3">Services for Organizations (NGOs & UN)</h3>
                    <p class="text-slate-600 text-sm mb-6 leading-relaxed">Strategic Monitoring & Evaluation (M&E) systems, humanitarian grant proposals, and epidemiologic assessments.</p>
                    
                    <ul class="space-y-3 text-sm text-slate-700">
                        <li class="flex items-start gap-3">
                            <i class="fa-solid fa-circle-check text-emerald-500 mt-1"></i>
                            <span><strong>Humanitarian Grant Proposals:</strong> Evidence-based narrative, logframes, and Theory of Change models.</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fa-solid fa-circle-check text-emerald-500 mt-1"></i>
                            <span><strong>M&E Systems & Dashboards:</strong> Custom performance indicators, Power BI, and DHIS2 integrations.</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fa-solid fa-circle-check text-emerald-500 mt-1"></i>
                            <span><strong>Outbreak Situation Analysis:</strong> Rapid risk assessments in conflict and fragile contexts.</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fa-solid fa-circle-check text-emerald-500 mt-1"></i>
                            <span><strong>Capacity Building Workshops:</strong> Staff training in digital surveillance tools and data literacy.</span>
                        </li>
                    </ul>

                    <div class="mt-8 pt-6 border-t border-slate-100">
                        <a href="#contact" class="inline-flex items-center text-sm font-semibold text-emerald-600 hover:text-emerald-700">
                            Request Institutional Consultancy <i class="fa-solid fa-arrow-right ml-2"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CLIENT REVIEWS / TESTIMONIALS SECTION -->
    <section id="reviews" class="py-16 md:py-24 bg-white border-t border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-xs font-bold uppercase tracking-wider text-brand-600 mb-2">Testimonials</h2>
                <p class="text-3xl font-bold text-slate-900">Client & Research Partner Reviews</p>
                <p class="mt-3 text-slate-600">Feedback from postgraduate scholars, NGO leaders, and public health collaborators.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                
                <!-- Review Card 1 -->
                <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200 space-y-4">
                    <div class="flex text-amber-400 gap-1 text-sm">
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                    </div>
                    <p class="text-sm text-slate-700 leading-relaxed italic">
                        "Mohamed's biostatistical and GIS analysis guidance transformed our outbreak evaluation manuscript. His mastery of R and epidemiological modeling ensured rapid publication."
                    </p>
                    <div class="pt-3 border-t border-slate-200">
                        <h4 class="font-bold text-slate-900 text-sm">Postgraduate Researcher</h4>
                        <span class="text-xs text-slate-500">Master of Public Health Candidate</span>
                    </div>
                </div>

                <!-- Review Card 2 -->
                <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200 space-y-4">
                    <div class="flex text-amber-400 gap-1 text-sm">
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                    </div>
                    <p class="text-sm text-slate-700 leading-relaxed italic">
                        "The grant proposal and logical framework designed by Mr. Mohamed secured vital funding for our emergency WASH and health response program. Exceptional detail and rigour."
                    </p>
                    <div class="pt-3 border-t border-slate-200">
                        <h4 class="font-bold text-slate-900 text-sm">Humanitarian Program Director</h4>
                        <span class="text-xs text-slate-500">International NGO</span>
                    </div>
                </div>

                <!-- Review Card 3 -->
                <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200 space-y-4">
                    <div class="flex text-amber-400 gap-1 text-sm">
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                    </div>
                    <p class="text-sm text-slate-700 leading-relaxed italic">
                        "His deep technical domain knowledge in DHIS2 integration and surveillance systems made our national public health reporting seamlessly effective."
                    </p>
                    <div class="pt-3 border-t border-slate-200">
                        <h4 class="font-bold text-slate-900 text-sm">Surveillance Lead</h4>
                        <span class="text-xs text-slate-500">Ministry / Public Health Institute</span>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- CONTACT FORM SECTION (FormSubmit Direct Integration) -->
    <section id="contact" class="py-16 md:py-24 bg-slate-900 text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
                
                <!-- Contact Info Column -->
                <div class="lg:col-span-5 space-y-6">
                    <span class="px-3 py-1 rounded-full bg-brand-500/20 text-brand-300 text-xs font-semibold uppercase tracking-wider">Get In Touch</span>
                    <h2 class="text-3xl font-extrabold text-white">Let's Collaborate on Data-Driven Public Health Solutions</h2>
                    <p class="text-slate-300 text-sm leading-relaxed">
                        Whether you are a student requiring research mentorship, an institution seeking strategic M&E/proposal expertise, or a research partner—reach out directly using the form or channels below.
                    </p>

                    <div class="space-y-4 pt-4">
                        <div class="flex items-center gap-4">
                            <div class="w-10 h-10 rounded-lg bg-slate-800 border border-slate-700 text-brand-400 flex items-center justify-center font-bold">
                                <i class="fa-solid fa-envelope"></i>
                            </div>
                            <div>
                                <span class="text-xs text-slate-400 block">Email Address</span>
                                <a href="mailto:medo.talib99@gmail.com" class="text-sm font-semibold text-white hover:text-brand-300">medo.talib99@gmail.com</a>
                            </div>
                        </div>

                        <div class="flex items-center gap-4">
                            <div class="w-10 h-10 rounded-lg bg-slate-800 border border-slate-700 text-emerald-400 flex items-center justify-center font-bold">
                                <i class="fa-brands fa-whatsapp"></i>
                            </div>
                            <div>
                                <span class="text-xs text-slate-400 block">Phone / WhatsApp</span>
                                <a href="https://wa.me/249912559111" class="text-sm font-semibold text-white hover:text-emerald-300">+249 912 559 111</a>
                            </div>
                        </div>

                        <div class="flex items-center gap-4">
                            <div class="w-10 h-10 rounded-lg bg-slate-800 border border-slate-700 text-sky-400 flex items-center justify-center font-bold">
                                <i class="fa-brands fa-linkedin-in"></i>
                            </div>
                            <div>
                                <span class="text-xs text-slate-400 block">LinkedIn Connection</span>
                                <a href="https://www.linkedin.com/in/mohamed-talib-664331158" target="_blank" class="text-sm font-semibold text-white hover:text-sky-300">linkedin.com/in/mohamed-talib-664331158</a>
                            </div>
                        </div>

                        <div class="flex items-center gap-4">
                            <div class="w-10 h-10 rounded-lg bg-slate-800 border border-slate-700 text-amber-400 flex items-center justify-center font-bold">
                                <i class="fa-solid fa-location-dot"></i>
                            </div>
                            <div>
                                <span class="text-xs text-slate-400 block">Current Location</span>
                                <span class="text-sm font-semibold text-white">Lusaka, Zambia (Africa CDC / ZNPHI)</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- FormSubmit Form Column -->
                <div class="lg:col-span-7 bg-slate-800 p-8 rounded-2xl border border-slate-700 shadow-2xl">
                    <h3 class="text-xl font-bold text-white mb-6">Send a Direct Message or Inquiry</h3>

                    <form action="https://formsubmit.co/medo.talib99@gmail.com" method="POST" enctype="multipart/form-data" class="space-y-5">
                        <!-- FormSubmit Configuration Settings -->
                        <input type="hidden" name="_subject" value="New Inquiry from Portfolio Website!">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="hidden" name="_template" value="table">

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                            <div>
                                <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">Your Full Name</label>
                                <input type="text" name="name" required placeholder="Dr. / Mr. / Ms. Name" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-brand-500">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">Email Address or Organization</label>
                                <input type="email" name="email" required placeholder="name@organization.org" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-brand-500">
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">Inquiry Category</label>
                            <select name="inquiry_type" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-brand-500">
                                <option value="Student Research Support">Student Research & Thesis Support (PhD / MSc)</option>
                                <option value="Institutional M&E Consultancy">Services for Organizations (M&E / Proposals)</option>
                                <option value="Public Health AI & Data Collaboration">Public Health AI & Data Science Collaboration</option>
                                <option value="General Inquiry">General Inquiry</option>
                            </select>
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">Your Message / Research Synopsis</label>
                            <textarea name="message" rows="4" required placeholder="Please outline your project, dataset requirements, or consultancy scope..." class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-brand-500"></textarea>
                        </div>

                        <div>
                            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">Attach Document / Synopsis / CV (PDF or Image)</label>
                            <input type="file" name="attachment" accept=".pdf,.png,.jpg,.jpeg" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-2 text-xs text-slate-400 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-xs file:font-semibold file:bg-brand-600 file:text-white hover:file:bg-brand-700">
                        </div>

                        <button type="submit" class="w-full py-3.5 bg-gradient-to-r from-brand-500 to-brand-600 text-white font-bold rounded-xl shadow-lg shadow-brand-500/20 hover:from-brand-600 hover:to-brand-700 transition flex items-center justify-center gap-2">
                            <i class="fa-solid fa-paper-plane"></i> Send Inquiry Directly
                        </button>
                    </form>
                </div>

            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="bg-slate-950 text-slate-400 py-8 border-t border-slate-800 text-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row justify-between items-center gap-4">
            <p>© 2026 Mohamed Mahmoud Talib, MSc. Public Health Informatics Professional.</p>
            <div class="flex gap-4">
                <a href="#home" class="hover:text-white transition">Back to Top</a>
                <a href="https://www.linkedin.com/in/mohamed-talib-664331158" target="_blank" class="hover:text-white transition">LinkedIn</a>
            </div>
        </div>
    </footer>

    <!-- JAVASCRIPT LOGIC -->
    <script>
        // Mobile Menu Toggle
        const menuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        menuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });

        // Tab Switching for Interactive Work
        function switchVizTab(tabId) {
            // Hide all tab content
            document.querySelectorAll('.viz-content').forEach(el => el.classList.add('hidden'));
            
            // Remove active style from buttons
            document.querySelectorAll('.viz-tab-btn').forEach(btn => {
                btn.classList.remove('bg-brand-600', 'text-white', 'shadow-sm');
                btn.classList.add('bg-slate-100', 'text-slate-600');
            });

            // Show selected content
            document.getElementById(`viz-${tabId}`).classList.remove('hidden');

            // Style active button
            const activeBtn = document.getElementById(`tab-btn-${tabId}`);
            activeBtn.classList.remove('bg-slate-100', 'text-slate-600');
            activeBtn.classList.add('bg-brand-600', 'text-white', 'shadow-sm');

            // Trigger Map refresh if spatial map selected
            if (tabId === 'spatial-map' && map) {
                setTimeout(() => { map.invalidateSize(); }, 200);
            }
        }

        // --- CHART.JS EPIDEMIC CURVE LOGIC ---
        let outbreakChart;
        let showIntervention = true;

        const weeks = ['Wk 1', 'Wk 2', 'Wk 3', 'Wk 4', 'Wk 5', 'Wk 6', 'Wk 7', 'Wk 8', 'Wk 9', 'Wk 10', 'Wk 11', 'Wk 12'];
        const gadarifCases = [12, 28, 45, 89, 120, 155, 172, 184, 110, 65, 32, 14];
        const chibomboCases = [5, 12, 22, 40, 68, 92, 105, 98, 54, 28, 15, 8];

        function initOutbreakChart() {
            const ctx = document.getElementById('outbreakChart').getContext('2d');
            
            outbreakChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: weeks,
                    datasets: [
                        {
                            label: 'Gadarif State (Sudan Outbreak)',
                            data: gadarifCases,
                            borderColor: '#0284c7',
                            backgroundColor: 'rgba(2, 132, 199, 0.1)',
                            fill: true,
                            tension: 0.3,
                            borderWidth: 3,
                            pointRadius: 4,
                            pointHoverRadius: 6
                        },
                        {
                            label: 'Chibombo / Kandindima (Zambia)',
                            data: chibomboCases,
                            borderColor: '#10b981',
                            backgroundColor: 'rgba(16, 185, 129, 0.1)',
                            fill: true,
                            tension: 0.3,
                            borderWidth: 3,
                            pointRadius: 4,
                            pointHoverRadius: 6
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { position: 'top' },
                        tooltip: {
                            mode: 'index',
                            intersect: false,
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: { display: true, text: 'Reported Weekly Cholera Cases' }
                        },
                        x: {
                            title: { display: true, text: 'Epidemiological Period (Weeks)' }
                        }
                    }
                }
            });
        }

        function updateEpidemicChart() {
            const val = document.getElementById('districtFilter').value;
            if (val === 'gadarif') {
                outbreakChart.data.datasets[0].hidden = false;
                outbreakChart.data.datasets[1].hidden = true;
            } else if (val === 'chibombo') {
                outbreakChart.data.datasets[0].hidden = true;
                outbreakChart.data.datasets[1].hidden = false;
            } else {
                outbreakChart.data.datasets[0].hidden = false;
                outbreakChart.data.datasets[1].hidden = false;
            }
            outbreakChart.update();
        }

        function toggleInterventionLine() {
            showIntervention = !showIntervention;
            alert(showIntervention ? "Intervention Marker Active: Oral Cholera Vaccine (OCV) & WASH campaign launched at Week 7." : "Intervention Markers Hidden.");
        }

        // --- PREDICTIVE RISK SIMULATOR LOGIC ---
        function calculateRisk() {
            const rain = parseInt(document.getElementById('sliderRainfall').value);
            const sanitation = parseInt(document.getElementById('sliderSanitation').value);
            const density = parseInt(document.getElementById('sliderDensity').value);
            const water = parseInt(document.getElementById('sliderWaterQuality').value);

            // Update Text Displays
            document.getElementById('valRainfall').innerText = `${rain} mm`;
            document.getElementById('valSanitation').innerText = `${sanitation} %`;
            document.getElementById('valDensity').innerText = density.toLocaleString();
            document.getElementById('valWaterQuality').innerText = water;

            // Simplified Outbreak Risk Formula
            let score = Math.round((rain * 0.25) + ((100 - sanitation) * 0.35) + ((density / 5000) * 20) + ((100 - water) * 0.20));
            score = Math.min(100, Math.max(0, score));

            document.getElementById('riskScoreText').innerText = score;

            const badge = document.getElementById('riskBadgeColor');
            const levelBox = document.getElementById('riskLevelBox');
            const rec = document.getElementById('riskRecommendation');

            if (score >= 70) {
                badge.className = "w-36 h-36 rounded-full border-8 border-red-500 flex flex-col items-center justify-center shadow-inner transition-colors duration-300";
                levelBox.className = "p-3 rounded-lg bg-red-100 text-red-800 font-bold text-sm";
                levelBox.innerText = "CRITICAL OUTBREAK RISK LEVEL";
                rec.innerText = "Action Plan: Rapid deployment of emergency water chlorination kits, health advisory broadcasts, and preemptive hospital bed allocation.";
            } else if (score >= 40) {
                badge.className = "w-36 h-36 rounded-full border-8 border-amber-500 flex flex-col items-center justify-center shadow-inner transition-colors duration-300";
                levelBox.className = "p-3 rounded-lg bg-amber-100 text-amber-800 font-bold text-sm";
                levelBox.innerText = "MODERATE RISK LEVEL";
                rec.innerText = "Action Plan: Enhanced community-based surveillance, weekly water source testing, and stocking oral rehydration salts (ORS).";
            } else {
                badge.className = "w-36 h-36 rounded-full border-8 border-emerald-500 flex flex-col items-center justify-center shadow-inner transition-colors duration-300";
                levelBox.className = "p-3 rounded-lg bg-emerald-100 text-emerald-800 font-bold text-sm";
                levelBox.innerText = "LOW OUTBREAK RISK";
                rec.innerText = "Action Plan: Routine surveillance monitoring and maintenance of standard sanitation practices.";
            }
        }

        // --- LEAFLET GEOSPATIAL MAP LOGIC ---
        let map;
        function initMap() {
            map = L.map('leaflet-map').setView([-15.4167, 28.2833], 5); // Default Lusaka, Zambia

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; OpenStreetMap contributors'
            }).addTo(map);

            // Field Locations
            const locations = [
                { lat: -15.4167, lng: 28.2833, title: "Lusaka (Africa CDC / ZNPHI Hub)", desc: "Primary base for public health informatics fellowships." },
                { lat: -14.9833, lng: 28.0667, title: "Chibombo District / Kandindima", desc: "Cholera outbreak evaluation and rural surveillance site." },
                { lat: 14.0323, lng: 35.3854, title: "Gadarif State (Sudan)", desc: "Field epidemiology and outbreak investigation baseline." }
            ];

            locations.forEach(loc => {
                L.marker([loc.lat, loc.lng]).addTo(map)
                    .bindPopup(`<b>${loc.title}</b><br>${loc.desc}`);
            });
        }

        function focusMap(coords, zoom) {
            map.setView(coords, zoom);
        }

        // --- PROJECT FILTER LOGIC ---
        function filterProjects(cat) {
            const cards = document.querySelectorAll('.project-card');
            cards.forEach(card => {
                if (cat === 'all' || card.getAttribute('data-category') === cat) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });

            document.querySelectorAll('.proj-filter-btn').forEach(btn => {
                btn.classList.remove('bg-brand-600', 'text-white');
                btn.classList.add('bg-white', 'text-slate-700');
            });
            event.target.classList.remove('bg-white', 'text-slate-700');
            event.target.classList.add('bg-brand-600', 'text-white');
        }

        // Initialize on load
        window.onload = function() {
            initOutbreakChart();
            calculateRisk();
            initMap();
        };
    </script>
</body>
</html>
