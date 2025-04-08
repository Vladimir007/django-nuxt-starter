// noinspection JSUnusedGlobalSymbols

export default defineNuxtPlugin(async (nuxtApp) => {
  if (useCookie('sessionid').value) {
    await useAuthStore().fetchUser()
  }
})