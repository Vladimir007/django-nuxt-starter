// noinspection JSUnusedGlobalSymbols
export default defineNuxtRouteMiddleware(async (to, from) => {
    let toPath = to.path
    if (toPath !== '/' && toPath.endsWith('/')) {
        toPath = toPath.replace(/\/+$/, '') || '/';
    }

    const userStore = useUserStore()
    if (!userStore.loaded && useCookie('sessionid').value) {
        await userStore.fetchSelfInfo()
    }

    const authStore = useAuthStore()
    if (authStore.isAuthenticated && (toPath === '/auth/login' || toPath === '/auth/register')) {
        return navigateTo('/')
    }
    if (!authStore.isAuthenticated && toPath !== '/auth/login' && toPath !== '/auth/register') {
        return navigateTo({
            path: '/auth/login',
            query: {
                next: to.fullPath
            }
        })
    }
})