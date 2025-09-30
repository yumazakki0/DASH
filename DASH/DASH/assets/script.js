/* tsparticles library precisa ser incluída no seu index.html ou via assets */
tsParticles.load("tsparticles", {
    fpsLimit: 60,
    background: { color: "#0f0f1f" },
    particles: {
        number: { value: 80, density: { enable: true, area: 800 } },
        color: { value: "#00aaff" },
        shape: { type: "circle" },
        opacity: { value: 0.5, random: false },
        size: { value: 3, random: true },
        links: { enable: true, distance: 150, color: "#00aaff", opacity: 0.4, width: 1 },
        move: { enable: true, speed: 2, direction: "none", random: false, straight: false, outModes: "out" }
    },
    detectRetina: true
});
