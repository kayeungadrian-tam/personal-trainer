<template>
    <div class="particles">
        <Particles id="tsparticles"
            :particlesInit="particlesInit"
            :particlesLoaded="particlesLoaded"
            :options=options />
    </div>
</template>

<style scoped>
.particles {
    z-index: -10
}
</style>


<script setup lang="ts">
import { loadFull } from "tsparticles";
import { ref } from "vue";


const particlesInit = async (engine: any) => {
    await loadFull(engine);
};

const particlesLoaded = async (container: any) => {
    console.log("Particles container loaded", container);
};

const options = ref(
    {
        background: {
            color: {
                value: 'transparent',
            }
        },
        fpsLimit: 120,
        interactivity: {
            events: {
                onClick: {
                    enable: false,
                    mode: 'push'
                },
                onHover: {
                    enable: false,
                    mode: 'repulse'
                },
                resize: true
            },
            modes: {
                bubble: {
                    distance: 400,
                    duration: 2,
                    opacity: 8,
                    size: 40,
                    speed: 3
                },
                push: {
                    quantity: 4
                },
                repulse: {
                    distance: 200,
                    duration: 0.4
                }
            }
        },
        particles: {
            number: { value: 8, density: { enable: true, value_area: 800 } },
            color: { value: "#25ADD651" },
            shape: {
                type: "polygon",
                stroke: { width: 0, color: "rgba(255,255,255,0.1)" },
                polygon: { nb_sides: 6 },
                image: { src: "img/github.svg", width: 100, height: 100 }
            },
            size: {
                value: 120,
                anim: {
                    enable: true,
                    speed: 10,
                    size_min: 50,
                    sync: false
                }
            },
            opacity: {
                value: 0.05,
                random: true,
                anim: {
                    enable: false, speed: 0.2, opacity_min: 0,
                    sync: false
                }
            },
            // links: {
            //     color: '#ffffff',
            //     distance: 150,
            //     enable: true,
            //     opacity: 0.5,
            //     width: 1
            // },
        },
        detectRetina: true
    }
);


</script>


<style scoped>
#particles-js {
    background: black;
    height: 100%;
    width: 100%;
}
</style>
