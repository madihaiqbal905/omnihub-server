import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate-script', methods=['POST'])
def generate_script():
    # 1. Grab structural data streamed out from Roblox
    game_info = request.json or {}
    game_name = game_info.get('GameName', 'Unknown Game')
    remotes = game_info.get('Remotes', [])

    print(f"\n[AI-CLOUD] Connected to Game: {game_name}")
    print(f"[AI-CLOUD] Scanning {len(remotes)} native Remote Events...")

    # 2. Automated Script Layout generation string passback
    ai_generated_code = f"""
    local Library = loadstring(game:HttpGet("https://githubusercontent.com"))()
    local Window = Library:CreateWindow({{ Title = 'AI Hub: {game_name}', Center = true, AutoShow = true }})
    local Tab = Window:AddTab('Main Panel')
    local Group = Tab:AddLeftGroupbox('AI Auto-Generated Automation')
    
    Group:AddLabel('Active Matrix: {game_name}')
    Group:AddLabel('Found Network Path Remotes: {len(remotes)}')
    
    Group:AddSlider('SpeedSlider', {{
        Text = 'Character Speed Boost', Default = 16, Min = 16, Max = 150, Round = 0,
        Callback = function(v) pcall(function() game.Players.LocalPlayer.Character.Humanoid.WalkSpeed = v end) end
    }})
    
    Library:SetWatermark('OmniHub Online Cloud Active')
    """
    
    return jsonify({"GeneratedScript": ai_generated_code})

if __name__ == '__main__':
    # Render assigns a port dynamically using an environment variable. 
    # Using os.environ.get ensures your app binds to the correct port online.
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
