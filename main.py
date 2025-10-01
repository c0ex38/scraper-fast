import os
from fastapi import FastAPI, Request, Form
from dotenv import load_dotenv
from firecrawl import Firecrawl

from fastapi.responses import HTMLResponse

# .env dosyası okunuyor
load_dotenv()
# Firecrawl için API anahtarı
API_KEY = os.getenv("API_KEY")

# Firecrawl istemcisi başlatılıyor
firecrawl = Firecrawl(api_key=API_KEY)

# FastAPI uygulaması oluşturuluyor
app = FastAPI(title="Firecrawl FastAPI Wrapper")


# Basit HTML formu sunan ana sayfa
@app.get("/", response_class=HTMLResponse)
def home():
    """
    Basit bir HTML formu döner. Kullanıcıdan scrape edilecek URL'i alır.
    """
    return """
    <!DOCTYPE html>
    <html lang=\"tr\">
    <h                .btn-secondary{
          background:rgba(99,102,241,0.1);
          color:var(--pri);
          border:1px solid var(--pri);
          position:relative;
        }
        .btn-secondary:hover{
          background:rgba(99,102,241,0.2);
          border-color:var(--pri-hover);
        }
        .btn-secondary:active{
          transform:scale(0.95);
        }
        .btn.copied{
          background:rgba(16,185,129,0.2);
          border-color:#10b981;
          color:#10b981;
        }
        .btn.copied::before{
          content:'✓ ';
        }         background:rgba(99,102,241,0.05);
          border:1px solid rgba(99,102,241,0.2);
          padding:12px 20px;
          border-radius:10px;
          font-size:13px;
          transition:all 0.3s ease;
          animation:slideUp 0.6s ease-out backwards;
        }
        .stat:nth-child(1){animation-delay:0.1s}
        .stat:nth-child(2){animation-delay:0.2s}
        .stat:hover{
          background:rgba(99,102,241,0.1);
          transform:translateY(-2px);
          box-shadow:0 4px 12px rgba(99,102,241,0.15);
        }
        .stat strong{
          color:var(--pri);
          font-weight:600;
        }
        @keyframes countUp{
          from{opacity:0;transform:translateY(10px)}
          to{opacity:1;transform:translateY(0)}
        }<meta charset=\"UTF-8\" />
      <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
      <title>Firecrawl Scraper - Web'i Markdown'a Dönüştür</title>
      <link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap\" rel=\"stylesheet\">
      <style>
        :root{
          --bg:#0a0e27;
          --card:#141b3d;
          --card-hover:#1a2347;
          --txt:#e8eaed;
          --muted:#9ca3af;
          --pri:#6366f1;
          --pri-hover:#4f46e5;
          --accent:#ec4899;
          --border:#2d3748;
        }
        *{box-sizing:border-box;margin:0;padding:0}
        @keyframes float{
          0%,100%{transform:translateY(0px)}
          50%{transform:translateY(-20px)}
        }
        @keyframes pulse{
          0%,100%{opacity:0.6}
          50%{opacity:0.8}
        }
        @keyframes slideUp{
          from{opacity:0;transform:translateY(30px)}
          to{opacity:1;transform:translateY(0)}
        }
        @keyframes shimmer{
          0%{background-position:200% 0}
          100%{background-position:-200% 0}
        }
        @keyframes gradientShift{
          0%,100%{background-position:0% 50%}
          50%{background-position:100% 50%}
        }
        @keyframes spin{
          to{transform:rotate(360deg)}
        }
        body{
          font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
          background:linear-gradient(135deg,#0a0e27 0%,#1a1f3a 50%,#0f1629 100%);
          background-size:200% 200%;
          animation:gradientShift 15s ease infinite;
          color:var(--txt);
          min-height:100vh;
          display:flex;
          align-items:center;
          justify-content:center;
          position:relative;
          overflow-x:hidden;
        }
        body::before{
          content:'';
          position:absolute;
          width:500px;
          height:500px;
          background:radial-gradient(circle,rgba(99,102,241,0.2) 0%,transparent 70%);
          top:-200px;
          right:-200px;
          border-radius:50%;
          pointer-events:none;
          animation:float 8s ease-in-out infinite,pulse 4s ease-in-out infinite;
        }
        body::after{
          content:'';
          position:absolute;
          width:400px;
          height:400px;
          background:radial-gradient(circle,rgba(236,72,153,0.15) 0%,transparent 70%);
          bottom:-150px;
          left:-150px;
          border-radius:50%;
          pointer-events:none;
          animation:float 10s ease-in-out infinite reverse,pulse 5s ease-in-out infinite;
        }
        .wrap{
          max-width:900px;
          width:100%;
          margin:40px auto;
          padding:24px;
          position:relative;
          z-index:1;
          animation:slideUp 0.8s ease-out;
        }
        .logo{
          text-align:center;
          margin-bottom:30px;
          animation:slideUp 0.6s ease-out;
        }
        .logo h1{
          font-size:42px;
          font-weight:700;
          background:linear-gradient(135deg,#6366f1 0%,#ec4899 50%,#f59e0b 100%);
          background-size:200% auto;
          -webkit-background-clip:text;
          -webkit-text-fill-color:transparent;
          background-clip:text;
          margin-bottom:8px;
          animation:shimmer 3s linear infinite;
          letter-spacing:-0.5px;
        }
        .logo p{
          color:var(--muted);
          font-size:15px;
          animation:slideUp 0.8s ease-out 0.2s both;
        }
        .card{
          background:rgba(20,27,61,0.85);
          backdrop-filter:blur(30px);
          border:1px solid var(--border);
          border-radius:24px;
          padding:40px;
          box-shadow:0 20px 60px rgba(0,0,0,0.4),inset 0 1px 0 rgba(255,255,255,0.05);
          transition:all 0.4s cubic-bezier(0.4,0,0.2,1);
          position:relative;
          overflow:hidden;
          animation:slideUp 1s ease-out 0.3s both;
        }
        .card::before{
          content:'';
          position:absolute;
          top:0;
          left:-100%;
          width:100%;
          height:100%;
          background:linear-gradient(90deg,transparent,rgba(99,102,241,0.1),transparent);
          transition:left 0.6s ease;
        }
        .card:hover::before{
          left:100%;
        }
        .card:hover{
          transform:translateY(-8px) scale(1.01);
          box-shadow:0 30px 80px rgba(99,102,241,0.25),0 0 40px rgba(236,72,153,0.1),inset 0 1px 0 rgba(255,255,255,0.1);
          border-color:rgba(99,102,241,0.3);
        }
        h2{
          font-size:24px;
          margin-bottom:10px;
          font-weight:600;
        }
        .subtitle{
          color:var(--muted);
          margin-bottom:30px;
          font-size:15px;
          line-height:1.6;
        }
        .subtitle strong{
          color:var(--accent);
          font-weight:600;
        }
        form{
          display:flex;
          gap:12px;
          flex-wrap:wrap;
        }
        input[type=url]{
          flex:1;
          min-width:300px;
          padding:16px 20px;
          border-radius:12px;
          border:2px solid var(--border);
          background:rgba(10,14,39,0.5);
          color:var(--txt);
          font-size:15px;
          transition:all 0.3s ease;
          font-family:inherit;
        }
        input[type=url]:focus{
          outline:none;
          border-color:var(--pri);
          box-shadow:0 0 0 3px rgba(99,102,241,0.1);
        }
        input[type=url]::placeholder{
          color:var(--muted);
        }
        button{
          padding:16px 32px;
          border-radius:12px;
          border:none;
          background:linear-gradient(135deg,var(--pri) 0%,var(--pri-hover) 100%);
          color:white;
          font-weight:600;
          font-size:15px;
          cursor:pointer;
          transition:all 0.3s cubic-bezier(0.4,0,0.2,1);
          box-shadow:0 4px 15px rgba(99,102,241,0.4);
          font-family:inherit;
          position:relative;
          overflow:hidden;
        }
        button::before{
          content:'';
          position:absolute;
          top:50%;
          left:50%;
          width:0;
          height:0;
          border-radius:50%;
          background:rgba(255,255,255,0.2);
          transform:translate(-50%,-50%);
          transition:width 0.6s,height 0.6s;
        }
        button:hover::before{
          width:300px;
          height:300px;
        }
        button:hover{
          transform:translateY(-3px) scale(1.02);
          box-shadow:0 8px 25px rgba(99,102,241,0.5),0 0 20px rgba(99,102,241,0.3);
        }
        button:active{
          transform:translateY(-1px) scale(0.98);
        }
        button.loading{
          pointer-events:none;
          opacity:0.7;
        }
        button.loading::after{
          content:'';
          position:absolute;
          width:16px;
          height:16px;
          top:50%;
          left:50%;
          margin:-8px 0 0 -8px;
          border:2px solid transparent;
          border-top-color:white;
          border-radius:50%;
          animation:spin 0.6s linear infinite;
        }
        .features{
          display:grid;
          grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
          gap:20px;
          margin-top:40px;
        }
        .feature{
          background:rgba(99,102,241,0.05);
          border:1px solid rgba(99,102,241,0.2);
          border-radius:16px;
          padding:24px;
          text-align:center;
          transition:all 0.4s cubic-bezier(0.4,0,0.2,1);
          position:relative;
          overflow:hidden;
        }
        .feature::before{
          content:'';
          position:absolute;
          top:-50%;
          left:-50%;
          width:200%;
          height:200%;
          background:radial-gradient(circle,rgba(99,102,241,0.1) 0%,transparent 70%);
          opacity:0;
          transition:opacity 0.4s ease;
        }
        .feature:hover::before{
          opacity:1;
        }
        .feature:hover{
          background:rgba(99,102,241,0.15);
          transform:translateY(-5px) scale(1.02);
          box-shadow:0 10px 30px rgba(99,102,241,0.2);
          border-color:rgba(99,102,241,0.4);
        }
        .feature-icon{
          font-size:40px;
          margin-bottom:12px;
          display:inline-block;
          transition:transform 0.4s ease;
          position:relative;
          z-index:1;
        }
        .feature:hover .feature-icon{
          transform:scale(1.1) rotate(5deg);
        }
        .feature h3{
          font-size:16px;
          margin-bottom:8px;
          color:var(--txt);
          position:relative;
          z-index:1;
        }
        .feature p{
          font-size:13px;
          color:var(--muted);
          line-height:1.5;
          position:relative;
          z-index:1;
        }
        footer{
          color:var(--muted);
          font-size:13px;
          margin-top:40px;
          text-align:center;
          opacity:0.7;
        }
        footer a{
          color:var(--pri);
          text-decoration:none;
        }
      </style>
    </head>
    <body>
      <div class=\"wrap\">
        <div class=\"logo\">
          <h1>🔥 Firecrawl Scraper</h1>
          <p>Web sayfalarını anında Markdown ve HTML'e dönüştürün</p>
        </div>
        <div class=\"card\">
          <h2>Hemen Başlayın</h2>
          <p class=\"subtitle\">Bir URL girin ve <strong>Firecrawl</strong> ile sayfanın içeriğini yapılandırılmış formatta alın.</p>
          <form method=\"post\" action=\"/scrape-ui\" onsubmit=\"handleSubmit(event)\">
            <input type=\"url\" name=\"url\" id=\"urlInput\" placeholder=\"https://ornek.com\" required />
            <button type=\"submit\" id=\"submitBtn\">
              <span id=\"btnText\">🚀 Scrape Et</span>
            </button>
          </form>
          <script>
            function handleSubmit(e) {
              const btn = document.getElementById('submitBtn');
              const btnText = document.getElementById('btnText');
              btn.classList.add('loading');
              btnText.textContent = 'İşleniyor...';
            }
          </script>
          <div class=\"features\">
            <div class=\"feature\">
              <div class=\"feature-icon\">📝</div>
              <h3>Markdown</h3>
              <p>Temiz, okunabilir markdown formatı</p>
            </div>
            <div class=\"feature\">
              <div class=\"feature-icon\">🌐</div>
              <h3>HTML</h3>
              <p>Tam kaynak HTML içeriği</p>
            </div>
            <div class=\"feature\">
              <div class=\"feature-icon\">⚡</div>
              <h3>Hızlı</h3>
              <p>Anında sonuç, sıfır gecikme</p>
            </div>
          </div>
        </div>
        <footer>Powered by <a href=\"https://firecrawl.dev\" target=\"_blank\">Firecrawl</a> • FastAPI ile geliştirildi</footer>
      </div>
    </body>
    </html>
    """


# Formdan gelen URL'i scrape edip sonuçları gösteren sayfa
@app.post("/scrape-ui", response_class=HTMLResponse)
async def scrape_ui(url: str = Form(...)):
    """
    Form ile gelen URL'i scrape eder; markdown ve HTML çıktısını tek sayfada gösterir.
    """
    if not API_KEY:
        return "<p style='color:#f66'>API_KEY bulunamadı. Lütfen .env içine API_KEY ekleyin.</p>"
    try:
        data = firecrawl.scrape(url, formats=["markdown", "html"])
        
        # Document nesnesinden attribute erişimi
        md_content = str(getattr(data, "markdown", ""))
        html_content = str(getattr(data, "html", ""))
        
        md = md_content.replace("<", "&lt;").replace(">", "&gt;").replace("{", "{{").replace("}", "}}")
        html_for_iframe = html_content.replace("\\", "\\\\").replace('"', "&quot;")
    except Exception as e:
        return f"""
        <html>
        <head>
          <meta charset='UTF-8'/>
          <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
          <style>
            body{{
              font-family:'Inter',sans-serif;
              background:linear-gradient(135deg,#0a0e27 0%,#1a1f3a 100%);
              color:#e8eaed;
              min-height:100vh;
              display:flex;
              align-items:center;
              justify-content:center;
              padding:20px;
            }}
            .error-card{{
              background:rgba(20,27,61,0.8);
              backdrop-filter:blur(20px);
              border:1px solid #2d3748;
              border-radius:20px;
              padding:40px;
              max-width:600px;
              text-align:center;
            }}
            .error-icon{{font-size:64px;margin-bottom:20px}}
            h2{{
              font-size:28px;
              margin-bottom:16px;
              background:linear-gradient(135deg,#ef4444 0%,#dc2626 100%);
              -webkit-background-clip:text;
              -webkit-text-fill-color:transparent;
              background-clip:text;
            }}
            pre{{
              background:rgba(239,68,68,0.1);
              border:1px solid rgba(239,68,68,0.3);
              border-radius:12px;
              padding:20px;
              margin:20px 0;
              text-align:left;
              color:#fca5a5;
              overflow:auto;
              font-size:13px;
            }}
            .btn{{
              display:inline-block;
              padding:12px 24px;
              background:linear-gradient(135deg,#6366f1 0%,#4f46e5 100%);
              color:white;
              text-decoration:none;
              border-radius:10px;
              font-weight:600;
              margin-top:20px;
              transition:transform 0.3s ease;
            }}
            .btn:hover{{transform:translateY(-2px)}}
          </style>
        </head>
        <body>
          <div class='error-card'>
            <div class='error-icon'>⚠️</div>
            <h2>Bir Hata Oluştu</h2>
            <p style='color:#9ca3af;margin-bottom:20px'>Scrape işlemi sırasında bir sorun yaşandı:</p>
            <pre>{e}</pre>
            <a href='/' class='btn'>🏠 Ana Sayfaya Dön</a>
          </div>
        </body>
        </html>
        """
    return f"""
    <!DOCTYPE html>
    <html lang='tr'>
    <head>
      <meta charset='UTF-8'/>
      <meta name='viewport' content='width=device-width, initial-scale=1'/>
      <title>Sonuç - Firecrawl Scraper</title>
      <link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap\" rel=\"stylesheet\">
      <style>
        :root{{
          --bg:#0a0e27;
          --card:#141b3d;
          --txt:#e8eaed;
          --muted:#9ca3af;
          --pri:#6366f1;
          --pri-hover:#4f46e5;
          --accent:#ec4899;
          --border:#2d3748;
          --success:#10b981;
        }}
        *{{box-sizing:border-box;margin:0;padding:0}}
        body{{
          font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
          background:linear-gradient(135deg,#0a0e27 0%,#1a1f3a 100%);
          color:var(--txt);
          min-height:100vh;
          padding:40px 20px;
        }}
        .wrap{{max-width:1200px;margin:0 auto}}
        .header{{
          text-align:center;
          margin-bottom:30px;
        }}
        .header h1{{
          font-size:32px;
          font-weight:700;
          background:linear-gradient(135deg,#6366f1 0%,#ec4899 100%);
          -webkit-background-clip:text;
          -webkit-text-fill-color:transparent;
          background-clip:text;
          margin-bottom:12px;
        }}
        .source-info{{
          display:inline-flex;
          align-items:center;
          gap:8px;
          background:rgba(16,185,129,0.1);
          border:1px solid rgba(16,185,129,0.3);
          padding:10px 16px;
          border-radius:8px;
          font-size:14px;
          color:var(--success);
          margin-bottom:20px;
        }}
        .source-info a{{
          color:var(--success);
          text-decoration:none;
          font-weight:500;
        }}
        .source-info a:hover{{
          text-decoration:underline;
        }}
        .card{{
          background:rgba(20,27,61,0.8);
          backdrop-filter:blur(20px);
          border:1px solid var(--border);
          border-radius:20px;
          padding:30px;
          box-shadow:0 20px 60px rgba(0,0,0,0.3);
        }}
        .tabs{{
          display:flex;
          gap:12px;
          margin-bottom:20px;
          border-bottom:2px solid var(--border);
          padding-bottom:0;
        }}
        .tabs button{{
          background:transparent;
          border:none;
          color:var(--muted);
          padding:12px 24px;
          font-size:15px;
          font-weight:600;
          cursor:pointer;
          border-radius:8px 8px 0 0;
          transition:all 0.3s ease;
          position:relative;
          font-family:inherit;
        }}
        .tabs button.active{{
          color:var(--pri);
          background:rgba(99,102,241,0.1);
        }}
        .tabs button.active::after{{
          content:'';
          position:absolute;
          bottom:-2px;
          left:0;
          right:0;
          height:2px;
          background:var(--pri);
        }}
        .tabs button:hover{{
          color:var(--txt);
          background:rgba(99,102,241,0.05);
        }}
        .tab-content{{
          display:none;
          animation:fadeIn 0.3s ease;
        }}
        .tab-content.active{{
          display:block;
        }}
        @keyframes fadeIn{{
          from{{opacity:0;transform:translateY(10px)}}
          to{{opacity:1;transform:translateY(0)}}
        }}
        pre{{
          white-space:pre-wrap;
          word-wrap:break-word;
          background:rgba(10,14,39,0.5);
          border:1px solid var(--border);
          border-radius:12px;
          padding:20px;
          max-height:70vh;
          overflow:auto;
          font-size:14px;
          line-height:1.6;
          font-family:'Fira Code','Consolas','Monaco',monospace;
        }}
        pre::-webkit-scrollbar{{
          width:8px;
          height:8px;
        }}
        pre::-webkit-scrollbar-track{{
          background:rgba(0,0,0,0.2);
          border-radius:4px;
        }}
        pre::-webkit-scrollbar-thumb{{
          background:var(--pri);
          border-radius:4px;
        }}
        iframe{{
          width:100%;
          height:70vh;
          border:1px solid var(--border);
          border-radius:12px;
          background:white;
        }}
        .actions{{
          display:flex;
          gap:12px;
          margin-top:24px;
          flex-wrap:wrap;
        }}
        .btn{{
          display:inline-flex;
          align-items:center;
          gap:8px;
          padding:12px 24px;
          border-radius:10px;
          text-decoration:none;
          font-weight:600;
          font-size:14px;
          transition:all 0.3s ease;
          border:none;
          cursor:pointer;
          font-family:inherit;
        }}
        .btn-primary{{
          background:linear-gradient(135deg,var(--pri) 0%,var(--pri-hover) 100%);
          color:white;
          box-shadow:0 4px 15px rgba(99,102,241,0.3);
        }}
        .btn-primary:hover{{
          transform:translateY(-2px);
          box-shadow:0 6px 20px rgba(99,102,241,0.4);
        }}
        .btn-secondary{{
          background:rgba(99,102,241,0.1);
          color:var(--pri);
          border:1px solid var(--pri);
        }}
        .btn-secondary:hover{{
          background:rgba(99,102,241,0.2);
        }}
        .stats{{
          display:flex;
          gap:20px;
          margin-bottom:20px;
          flex-wrap:wrap;
        }}
        .stat{{
          background:rgba(99,102,241,0.05);
          border:1px solid rgba(99,102,241,0.2);
          padding:12px 20px;
          border-radius:10px;
          font-size:13px;
        }}
        .stat strong{{
          color:var(--pri);
          font-weight:600;
        }}
      </style>
      <script>
        function showTab(tabName){{
          document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
          document.querySelectorAll('.tabs button').forEach(el => el.classList.remove('active'));
          document.getElementById('tab-' + tabName).classList.add('active');
          document.getElementById('btn-' + tabName).classList.add('active');
        }}
        function copyContent(tabName, btn){{
          let content;
          if (tabName === 'md') {{
            content = document.querySelector('#tab-md pre').textContent;
          }} else {{
            content = document.querySelector('#tab-html iframe').srcdoc;
          }}
          navigator.clipboard.writeText(content).then(() => {{
            const originalText = btn.textContent;
            btn.classList.add('copied');
            btn.textContent = 'Kopyalandı!';
            setTimeout(() => {{
              btn.classList.remove('copied');
              btn.textContent = originalText;
            }}, 2000);
          }});
        }}
        window.addEventListener('DOMContentLoaded', function(){{ showTab('md'); }});
      </script>
    </head>
    <body>
      <div class='wrap'>
        <div class='header'>
          <h1>✨ Scrape Tamamlandı</h1>
          <div class='source-info'>
            <span>✓</span>
            <span>Kaynak:</span>
            <a href='{url}' target='_blank' rel='noopener'>{url}</a>
          </div>
        </div>
        <div class='card'>
          <div class='stats'>
            <div class='stat'><strong>Markdown:</strong> {{len(md_content)}} karakter</div>
            <div class='stat'><strong>HTML:</strong> {{len(html_content)}} karakter</div>
          </div>
          <div class='tabs'>
            <button id='btn-md' onclick=\"showTab('md')\">📝 Markdown</button>
            <button id='btn-html' onclick=\"showTab('html')\">🌐 HTML Önizleme</button>
          </div>
          <div id='tab-md' class='tab-content'>
            <pre>{md}</pre>
          </div>
          <div id='tab-html' class='tab-content'>
            <iframe srcdoc="{html_for_iframe}"></iframe>
          </div>
          <div class='actions'>
            <a href='/' class='btn btn-primary'>🏠 Ana Sayfa</a>
            <button onclick=\"copyContent('md', this)\" class='btn btn-secondary'>📋 Markdown Kopyala</button>
            <button onclick=\"copyContent('html', this)\" class='btn btn-secondary'>📋 HTML Kopyala</button>
          </div>
        </div>
      </div>
    </body>
    </html>
    """

@app.get("/scrape")
def scrape_site(url: str):
    """
    URL parametresi alır, belirtilen sayfanın içeriğini markdown ve HTML olarak döner.
    Tek bir sayfanın içeriğini hızlıca scrape etmek için kullanılır.
    """
    data = firecrawl.scrape(url, formats=["markdown", "html"])
    # Document nesnesini dict'e çevir
    return {
        "markdown": getattr(data, "markdown", ""),
        "html": getattr(data, "html", ""),
        "metadata": getattr(data, "metadata", None)
    }

@app.get("/crawl")
def crawl_site(url: str, limit: int = 10):
    """
    URL parametresi ve limit alır, verilen siteyi belirtilen sayfa sayısı limitiyle tarar 
    ve dönen veriyi markdown+HTML formatında döner.
    Siteyi bloklayıcı şekilde crawl etmek için kullanılır.
    """
    result = firecrawl.crawl(
        url,
        limit=limit,
        scrape_options={"formats": ["markdown", "html"]},
    )
    return result