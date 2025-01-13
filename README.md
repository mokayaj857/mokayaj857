<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>John Mokaya - Portfolio</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/typed.js/2.0.12/typed.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background: linear-gradient(to bottom right, #0a192f, #112240);
            color: #e2e8f0;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .header {
            text-align: center;
            margin-bottom: 3rem;
            animation: fadeIn 1s ease-in;
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #64ffda;
        }

        .header h3 {
            color: #8892b0;
            font-size: 1.2rem;
        }

        .info-section {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 2rem;
            margin-bottom: 2rem;
            backdrop-filter: blur(10px);
            animation: slideUp 1s ease-out;
        }

        .info-item {
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .info-item span {
            color: #64ffda;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin: 2rem 0;
        }

        .social-link {
            color: #64ffda;
            text-decoration: none;
            padding: 0.5rem 1rem;
            border: 1px solid #64ffda;
            border-radius: 5px;
            transition: all 0.3s ease;
        }

        .social-link:hover {
            background: #64ffda20;
            transform: translateY(-3px);
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }

        .stats-item {
            background: rgba(255, 255, 255, 0.05);
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
        }

        .stats-item img {
            width: 100%;
            height: auto;
            border-radius: 5px;
        }

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }

        .skill-item {
            background: rgba(255, 255, 255, 0.05);
            padding: 0.8rem;
            border-radius: 5px;
            text-align: center;
            transition: all 0.3s ease;
        }

        .skill-item:hover {
            transform: translateY(-5px);
            background: rgba(100, 255, 218, 0.1);
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .snake-contribution {
            width: 100%;
            margin: 2rem 0;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 1rem;
        }

        .support-button {
            display: inline-block;
            background: #64ffda;
            color: #0a192f;
            padding: 0.8rem 2rem;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s ease;
            margin-top: 2rem;
        }

        .support-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(100, 255, 218, 0.3);
        }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1 id="typing-text"></h1>
            <h3>A passionate software developer from Kenya</h3>
        </header>

        <section class="info-section">
            <div class="info-item">
                <span>🔭</span> Currently working on: <strong>HerdSecure IoT Project</strong>
            </div>
            <div class="info-item">
                <span>🌱</span> Learning: <strong>JavaScript, React Native, MySQL</strong>
            </div>
            <div class="info-item">
                <span>💬</span> Ask me about: <strong>Node.js, React, Firebase</strong>
            </div>
            <div class="info-item">
                <span>⚡</span> Fun fact: <strong>Game of Thrones Night's Watch cloaks are made from Ikea rugs</strong>
            </div>
        </section>

        <div class="social-links">
            <a href="mailto:mokayaj857@gmail.com" class="social-link">Email</a>
            <a href="https://linkedin.com/in/john-mokaya-3b926a261" class="social-link">LinkedIn</a>
            <a href="https://john-mokaya.vercel.app/" class="social-link">Portfolio</a>
            <a href="https://github.com/mokayaj857" class="social-link">GitHub</a>
        </div>

        <section class="stats-grid">
            <div class="stats-item">
                <img src="https://github-readme-streak-stats.herokuapp.com/?user=mokayaj857&theme=dark&hide_border=true" alt="GitHub Streak">
            </div>
            <div class="stats-item">
                <img src="https://github-readme-stats.vercel.app/api?username=mokayaj857&show_icons=true&theme=dark&hide_border=true" alt="GitHub Stats">
            </div>
        </section>

        <h2 style="text-align: center; color: #64ffda; margin: 2rem 0;">⚒️ Skills</h2>
        <div class="skills-grid">
            <div class="skill-item">React</div>
            <div class="skill-item">Node.js</div>
            <div class="skill-item">JavaScript</div>
            <div class="skill-item">Python</div>
            <div class="skill-item">Firebase</div>
            <div class="skill-item">MySQL</div>
            <div class="skill-item">Next.js</div>
            <div class="skill-item">HTML/CSS</div>
        </div>

        <div class="snake-contribution">
            <img src="https://raw.githubusercontent.com/mokayaj857/mokayaj857/output/github-contribution-grid-snake.svg" alt="snake eating contributions" style="width: 100%;">
        </div>

        <div style="text-align: center;">
            <a href="https://ko-fi.com/V7V4RAK9C" class="support-button">
                Support My Work ☕
            </a>
        </div>
    </div>

    <script>
        new Typed('#typing-text', {
            strings: ["Hi There! 👋", "I'm John Mokaya!"],
            typeSpeed: 50,
            backSpeed: 50,
            loop: true
        });
    </script>
</body>
</html>
