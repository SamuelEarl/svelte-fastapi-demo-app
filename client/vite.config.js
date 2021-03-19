import { defineConfig } from "vite";
import svelte from "@svitejs/vite-plugin-svelte";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    proxy: {
      "/api": "http://localhost:8000"
    }
  }
});