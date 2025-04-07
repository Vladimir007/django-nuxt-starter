<script setup lang="ts">
useHead({
  script: [
    {
      children: `
      if (localStorage.theme === "dark" || !("theme" in localStorage)) {
        document.documentElement.classList.add('p-dark')
      } else {
        document.documentElement.classList.remove('p-dark')
      }`
    }
  ]
})

const route = useRoute()
const authStore = useAuthStore()

authStore.$subscribe(async (mutation, state) => {
  if (!state.isAuthenticated) {
    const sessionCookie = useCookie('sessionid')
    sessionCookie.value = null
    await navigateTo({path: '/auth/login', query: {next: route.fullPath}})
  }
})
</script>

<template>
  <div class="bg-surface-100 dark:bg-surface-800 min-h-screen p-2">
    <Toast />
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>
