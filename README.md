import React, { useState, useEffect } from 'react';
import { Github, Linkedin, Mail, Globe, Code, Database, Server, Layout } from 'lucide-react';

const PortfolioReadme = () => {
  const [isVisible, setIsVisible] = useState(false);
  const [currentText, setCurrentText] = useState('');
  const fullText = "Hi There! 👋 I'm John Mokaya!";
  const [hoverSkill, setHoverSkill] = useState(null);

  useEffect(() => {
    setIsVisible(true);
    let index = 0;
    const timer = setInterval(() => {
      if (index < fullText.length) {
        setCurrentText(prev => prev + fullText.charAt(index));
        index++;
      } else {
        clearInterval(timer);
      }
    }, 100);
    return () => clearInterval(timer);
  }, []);

  const rotateIn = "opacity-0 rotate-x-90 " + (isVisible ? "animate-rotateIn opacity-100 rotate-x-0" : "");
  const slideIn = "opacity-0 -translate-x-full " + (isVisible ? "animate-slideIn opacity-100 translate-x-0" : "");

  const skills = [
    { name: 'React', icon: <Layout className="w-6 h-6" />, color: 'bg-blue-500' },
    { name: 'Node.js', icon: <Server className="w-6 h-6" />, color: 'bg-green-500' },
    { name: 'JavaScript', icon: <Code className="w-6 h-6" />, color: 'bg-yellow-500' },
    { name: 'Firebase', icon: <Database className="w-6 h-6" />, color: 'bg-orange-500' },
    // Add more skills with their respective icons
  ];

  return (
    <div className="max-w-4xl mx-auto p-8 space-y-8 bg-gradient-to-br from-gray-900 via-blue-900 to-purple-900 text-white rounded-lg relative overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0 opacity-20">
        <div className="absolute w-72 h-72 bg-blue-500 rounded-full blur-3xl animate-float top-0 left-0" />
        <div className="absolute w-72 h-72 bg-purple-500 rounded-full blur-3xl animate-float-delayed top-0 right-0" />
        <div className="absolute w-72 h-72 bg-pink-500 rounded-full blur-3xl animate-float-reverse bottom-0 left-0" />
      </div>

      {/* Typing Animation Header */}
      <header className="text-center space-y-4 relative z-10">
        <h1 className="text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400">
          {currentText}
          <span className="animate-blink">|</span>
        </h1>
        <h2 className="text-xl font-light tracking-wide animate-pulse">
          Software Developer | IoT Enthusiast | Based in Kenya
        </h2>
      </header>

      {/* 3D Rotating Work Cards */}
      <section className={`grid grid-cols-1 md:grid-cols-2 gap-6 ${rotateIn}`}>
        <div className="group perspective">
          <div className="relative preserve-3d group-hover:rotate-y-180 duration-1000">
            <div className="bg-gradient-to-br from-blue-500/20 to-purple-500/20 p-6 rounded-xl backdrop-blur-lg border border-white/10 absolute backface-hidden">
              <h3 className="text-xl font-bold mb-4">Current Project</h3>
              <p>HerdSecure IoT Project</p>
            </div>
            <div className="bg-gradient-to-br from-purple-500/20 to-pink-500/20 p-6 rounded-xl backdrop-blur-lg border border-white/10 absolute backface-hidden rotate-y-180">
              <h3 className="text-xl font-bold mb-4">Project Details</h3>
              <p>Advanced IoT solution for livestock management and security</p>
            </div>
          </div>
        </div>
        {/* Add more rotating cards */}
      </section>

      {/* Floating Skill Bubbles */}
      <section className="relative h-64 my-12">
        {skills.map((skill, index) => (
          <div
            key={skill.name}
            className={`absolute transform transition-all duration-500 ${skill.color} rounded-full p-4 hover:scale-125 cursor-pointer`}
            style={{
              left: `${(index * 25) % 80}%`,
              top: `${Math.sin(index) * 40 + 50}%`,
              animation: `float ${3 + index}s infinite ease-in-out`
            }}
            onMouseEnter={() => setHoverSkill(skill.name)}
            onMouseLeave={() => setHoverSkill(null)}
          >
            {skill.icon}
            <span className={`absolute top-full left-1/2 -translate-x-1/2 mt-2 opacity-0 transition-opacity duration-300 ${hoverSkill === skill.name ? 'opacity-100' : ''}`}>
              {skill.name}
            </span>
          </div>
        ))}
      </section>

      {/* Animated GitHub Stats */}
      <section className={`space-y-6 ${slideIn}`}>
        <h3 className="text-2xl font-bold text-center bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-400">
          GitHub Contributions
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="transform transition-all duration-500 hover:scale-105 hover:rotate-2">
            <img 
              className="w-full h-auto rounded-xl shadow-lg shadow-purple-500/20"
              src="https://github-readme-streak-stats.herokuapp.com/?user=mokayaj857&theme=dark&hide_border=true&background=0D1117"
              alt="GitHub Streak Stats"
            />
          </div>
          <div className="transform transition-all duration-500 hover:scale-105 hover:-rotate-2">
            <img 
              className="w-full h-auto rounded-xl shadow-lg shadow-blue-500/20"
              src="https://github-readme-stats.vercel.app/api?username=mokayaj857&show_icons=true&theme=dark&hide_border=true&background=0D1117"
              alt="GitHub Stats"
            />
          </div>
        </div>
      </section>

      {/* Animated Snake Contribution */}
      <section className="relative overflow-hidden rounded-xl backdrop-blur-lg border border-white/10">
        <div className="absolute inset-0 bg-gradient-to-r from-blue-500/10 to-purple-500/10" />
        <img 
          className="w-full h-auto relative z-10"
          src="https://raw.githubusercontent.com/mokayaj857/mokayaj857/output/github-contribution-grid-snake.svg"
          alt="snake eating contributions"
        />
      </section>

      {/* Glowing Social Links */}
      <section className="flex justify-center space-x-8">
        {[
          { icon: <Mail />, href: "mailto:mokayaj857@gmail.com", color: "from-blue-400 to-blue-600" },
          { icon: <Linkedin />, href: "https://linkedin.com/in/john-mokaya-3b926a261", color: "from-blue-500 to-blue-700" },
          { icon: <Globe />, href: "https://john-mokaya.vercel.app/", color: "from-purple-400 to-purple-600" },
          { icon: <Github />, href: "https://github.com/mokayaj857", color: "from-gray-400 to-gray-600" }
        ].map((link, index) => (
          <a
            key={index}
            href={link.href}
            target="_blank"
            rel="noopener noreferrer"
            className={`transform hover:scale-125 transition-all duration-300 p-3 rounded-full bg-gradient-to-r ${link.color} hover:shadow-lg hover:shadow-white/20 relative group`}
          >
            <div className="w-8 h-8 text-white group-hover:animate-spin-slow">
              {link.icon}
            </div>
            <div className="absolute -inset-1 bg-gradient-to-r from-white/20 to-transparent blur opacity-0 group-hover:opacity-100 transition-opacity rounded-full" />
          </a>
        ))}
      </section>

      {/* Support Button */}
      <footer className="text-center pt-8">
        <a 
          href="https://ko-fi.com/V7V4RAK9C" 
          target="_blank" 
          rel="noopener noreferrer"
          className="inline-block px-8 py-3 bg-gradient-to-r from-blue-500 to-purple-500 text-white rounded-full font-bold hover:shadow-lg hover:shadow-purple-500/50 transform hover:scale-110 transition-all duration-300 animate-pulse"
        >
          ☕ Support My Work
        </a>
      </footer>
    </div>
  );
};

// Add required CSS animations
const style = document.createElement('style');
style.textContent = `
  @keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
  }
  @keyframes float-delayed {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
  }
  @keyframes float-reverse {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(20px); }
  }
  @keyframes spin-slow {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }
  .backface-hidden {
    backface-visibility: hidden;
  }
  .preserve-3d {
    transform-style: preserve-3d;
  }
  .perspective {
    perspective: 1000px;
  }
`;
document.head.appendChild(style);

export default PortfolioReadme;
