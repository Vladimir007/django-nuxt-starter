// noinspection JSUnusedGlobalSymbols
export default defineNuxtPlugin(() => {
    const api = $fetch.create({
        ignoreResponseError: true,

        onRequest({options}) {
            const cookie = useRequestHeader('cookie')
            options.headers.set('cookie', cookie)
            const csrfToken = useCookie('csrftoken') || ''
            if (csrfToken) {
                options.headers.set('X-CSRFToken', csrfToken.value)
            }
        },

        async onResponse({response}) {
            let isFailed: boolean;
            const data = (response._data instanceof Object) ? response._data : {'detail': 'Unknown error'}

            switch (response.status) {
                case 200:
                case 201:
                    isFailed = false
                    break;
                case 404:
                    isFailed = true;
                    data.detail = 'Page not found'
                    break;
                case 401:
                case 403:
                    useAuthStore().setAuthenticated(false)
                    useUserStore().setSelfInfo()
                    isFailed = true;
                    break;
                default:
                    isFailed = true;
                    break;
            }
            response._data = {
                failed: isFailed,
                status: response.status,
                data: data
            }
        }
    })

    return {provide: {api}}
})