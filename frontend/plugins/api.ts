// noinspection JSUnusedGlobalSymbols
export default defineNuxtPlugin(() => {
  const unsafeMethods = new Set(['POST', 'PUT', 'PATCH', 'DELETE'])

  const api = $fetch.create({
    onRequest({options}) {
      const cookie = useRequestHeader('cookie')
      options.headers.set('cookie', cookie)

      if (unsafeMethods.has((options.method || 'GET').toUpperCase())) {
        const csrfToken = useCookie('csrftoken') || ''
        if (csrfToken) {
          options.headers.set('X-CSRFToken', csrfToken.value)
        }
      }
    },
    async onResponseError({ request, response }) {
      switch (response.status) {
        case 401:
        case 403:
          await useAuthStore().logout()
          break;
        default:
          break;
      }

      if (response.headers.get("content-type") !== "application/json") {
        response._data = {'detail': response.statusText}
      }
    }
  })

  return {provide: {api}}
})