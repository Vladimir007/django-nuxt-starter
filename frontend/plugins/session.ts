// noinspection JSUnusedGlobalSymbols

export default defineNuxtPlugin(async () => {
  if (process.client) {
    return
  }
  if (useCookie('sessionid').value) {
    await useAuthStore().fetchUser()
  }
})