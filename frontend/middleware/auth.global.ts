// noinspection JSUnusedGlobalSymbols
export default defineNuxtRouteMiddleware((to) => {
    let toPath = to.path
    if (toPath !== '/' && toPath.endsWith('/')) {
        toPath = toPath.replace(/\/+$/, '') || '/';
    }

    const authStore = useAuthStore()
    if (authStore.isAuthenticated && (toPath === '/auth/login' || toPath === '/auth/register')) {
        return navigateTo('/', {replace: true})
    }
    if (!authStore.isAuthenticated && toPath !== '/auth/login' && toPath !== '/auth/register') {
        return navigateTo({
            path: '/auth/login',
            query: {
                next: to.fullPath
            }
        }, {replace: true})
    }
})