import { defineStore } from 'pinia'

// noinspection JSUnusedGlobalSymbols
export const useAuthStore = defineStore('auth', () => {
  const user: Ref<IUser> = ref()

  const isAuthenticated: ComputedRef<boolean> = computed(() => !!user.value)

  const userLabel: ComputedRef<string> = computed(() => (
    user.value ? (user.value.first_name[0] + user.value.last_name[0]) : ""
  ))

  function setUser(data?: IUser) {
    user.value = data
  }

  async function fetchUser() {
    await useNuxtApp().$api('/api/accounts/account/').then((data) => {
      setUser(data)
    }).catch(() => {})
  }

  async function login(data: ICredentials) {
    return await useNuxtApp().$api('/api/accounts/login/', {
      method: 'POST',
      body: data,
    }).then(async (data) => {
      const route = useRoute()
      setUser(data)
      await navigateTo(route.query.next || '/', {replace: true})
    }).catch(error => error.data.detail)
  }

  async function logout() {
    await useNuxtApp().$api('/api/accounts/logout/', {method: 'POST', ignoreResponseError: true})
    setUser()
    useRouter().go(0)
  }

  async function register(data: IRegistrationForm) {
    return await useNuxtApp().$api('/api/accounts/account/', {
      method: 'POST',
      body: data,
    }).then(async () => {
      await navigateTo(
        {
          path: '/auth/login',
          query: {
            new: true
          }
        },
        {
          replace: true
        }
      )
    }).catch((error) => error.data)
  }

  async function updateUser(data: IUpdateProfileForm) {
    const requestBody: IUpdateProfileForm = {...data}
    if (!requestBody.password1 && !requestBody.password2) {
      delete requestBody.password1
      delete requestBody.password2
    }
    return await useNuxtApp().$api('/api/accounts/account/', {
      method: 'PATCH',
      body: requestBody,
    }).then(async () => {await fetchUser()}).catch(error => error.data)
  }

  return {
    user, isAuthenticated, userLabel, fetchUser, login, logout, register, updateUser
  }
})