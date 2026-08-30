<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" 
                xmlns:html="http://www.w3.org/TR/REC-html40"
                xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9"
                xmlns:xhtml="http://www.w3.org/1999/xhtml"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
      <head>
        <title>XML Sitemap – Burger King Breakfast Menu UK</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800&amp;family=Inter:wght@400;500;600&amp;display=swap" />
        <style type="text/css">
          * { box-sizing: border-box; margin: 0; padding: 0; }
          body {
            background-color: #0d0d0d;
            color: #e5e5e5;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 14px;
            line-height: 1.6;
            padding: 30px 20px;
          }
          .container {
            max-width: 1200px;
            margin: 0 auto;
          }
          .header {
            background: linear-gradient(135deg, #1c1c1c 0%, #141414 100%);
            border: 1px solid #2a2a2a;
            border-radius: 16px;
            padding: 32px;
            margin-bottom: 28px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.5);
          }
          .logo-area {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 12px;
          }
          .logo-icon {
            font-size: 28px;
            background: linear-gradient(135deg, #FF6B00, #F5A800);
            border-radius: 10px;
            width: 46px;
            height: 46px;
            display: flex;
            align-items: center;
            justify-content: center;
          }
          h1 {
            font-family: 'Outfit', sans-serif;
            font-size: 24px;
            font-weight: 800;
            background: linear-gradient(90deg, #FF6B00, #F5A800);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
          }
          .desc {
            color: #999999;
            font-size: 14px;
            margin-top: 6px;
          }
          .stats-bar {
            display: flex;
            gap: 16px;
            margin-top: 18px;
            flex-wrap: wrap;
          }
          .badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(255,107,0,0.12);
            border: 1px solid rgba(255,107,0,0.3);
            color: #FF6B00;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
          }
          .table-wrap {
            background: #141414;
            border: 1px solid #242424;
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 4px 24px rgba(0,0,0,0.4);
          }
          table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
          }
          th {
            background-color: #1a1a1a;
            color: #ffffff;
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 14px 18px;
            border-bottom: 1px solid #2a2a2a;
          }
          td {
            padding: 12px 18px;
            border-bottom: 1px solid #1f1f1f;
            font-size: 13px;
          }
          tr:hover td {
            background-color: rgba(255,107,0,0.04);
          }
          a {
            color: #FF6B00;
            text-decoration: none;
            font-weight: 500;
            word-break: break-all;
            transition: color 0.2s;
          }
          a:hover {
            color: #F5A800;
            text-decoration: underline;
          }
          .prio-pill {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 6px;
            font-weight: 700;
            font-size: 11px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            color: #e0e0e0;
          }
          .prio-high {
            background: rgba(255,107,0,0.18);
            border-color: rgba(255,107,0,0.4);
            color: #FF6B00;
          }
          .alts-container {
            display: flex;
            gap: 4px;
            flex-wrap: wrap;
          }
          .alt-tag {
            font-size: 11px;
            background: #202020;
            padding: 2px 6px;
            border-radius: 4px;
            border: 1px solid #2e2e2e;
            color: #cccccc;
          }
          .footer {
            margin-top: 28px;
            text-align: center;
            font-size: 12px;
            color: #666666;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="header">
            <div class="logo-area">
              <div class="logo-icon">🍔</div>
              <div>
                <h1>Burger King Breakfast Menu UK – XML Sitemap</h1>
                <p class="desc">Google-compliant international XML Sitemap with alternate hreflang tags.</p>
              </div>
            </div>
            <div class="stats-bar">
              <div class="badge">🌐 5 Languages: EN, ES, FR, DE, HI</div>
              <div class="badge">📄 <xsl:value-of select="count(sitemap:urlset/sitemap:url)"/> Total URLs</div>
              <div class="badge">⚡ Status: 100% Search Engine Optimized</div>
            </div>
          </div>

          <div class="table-wrap">
            <table>
              <thead>
                <tr>
                  <th style="width: 45px;">#</th>
                  <th>URL (Location)</th>
                  <th style="width: 220px;">Multilingual Alternates</th>
                  <th style="width: 110px;">Changefreq</th>
                  <th style="width: 90px;">Priority</th>
                </tr>
              </thead>
              <tbody>
                <xsl:for-each select="sitemap:urlset/sitemap:url">
                  <tr>
                    <td style="color:#666666;"><xsl:value-of select="position()"/></td>
                    <td>
                      <a href="{sitemap:loc}">
                        <xsl:value-of select="sitemap:loc"/>
                      </a>
                    </td>
                    <td>
                      <div class="alts-container">
                        <xsl:for-each select="xhtml:link[@hreflang!='x-default']">
                          <span class="alt-tag"><xsl:value-of select="@hreflang"/></span>
                        </xsl:for-each>
                      </div>
                    </td>
                    <td style="color:#999999;"><xsl:value-of select="sitemap:changefreq"/></td>
                    <td>
                      <xsl:variable name="prioVal" select="sitemap:priority"/>
                      <span class="prio-pill">
                        <xsl:if test="$prioVal &gt;= 0.8">
                          <xsl:attribute name="class">prio-pill prio-high</xsl:attribute>
                        </xsl:if>
                        <xsl:value-of select="sitemap:priority"/>
                      </span>
                    </td>
                  </tr>
                </xsl:for-each>
              </tbody>
            </table>
          </div>

          <div class="footer">
            <p>© 2024–2026 Burger King Breakfast Menu UK • burgerkingbreakfastmenu.co.uk</p>
          </div>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
