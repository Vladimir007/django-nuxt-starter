import Aura from '@primeuix/themes/aura'
import tailwindcss from "@tailwindcss/vite";
import { definePreset } from "@primeuix/themes";

const themePreset = definePreset(Aura, {
  semantic: {
    primary: {
      50: '{violet.50}',
      100: '{violet.100}',
      200: '{violet.200}',
      300: '{violet.300}',
      400: '{violet.400}',
      500: '{violet.500}',
      600: '{violet.600}',
      700: '{violet.700}',
      800: '{violet.800}',
      900: '{violet.900}',
    },
  },
})

// noinspection JSUnusedGlobalSymbols
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  app: {
    head: {
      title: "Django Nuxt Starter",
    }
  },
  modules: ['@primevue/nuxt-module', '@pinia/nuxt'],
  css: ['@/assets/css/main.css'],
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
  primevue: {
    options: {
      theme: {
        preset: themePreset,
        options: {
          darkModeSelector: ".p-dark",
        },
      },
      ripple: true,
    },
    autoImport: true,
  },
  nitro: {
    devProxy: {
      "/api": {
        target: "http://backend:8000/api",
        changeOrigin: true,
        prependPath: true,
      },
    },
    routeRules: {
      '/api/**': {
        proxy: "http://backend:8000/api/**",
      }
    },
  },
  devServer: {
    host: "0.0.0.0",
    port: 3000,
  },
})