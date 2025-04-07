import { defineStore } from 'pinia'

interface AccountUpdateData {
  first_name: string;
  last_name: string;
  password1?: string;
  password2?: string;
}

// noinspection JSUnusedGlobalSymbols
export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: false
  }),
  actions: {
    async login(credentials) {
      const { $api } = useNuxtApp()
      const response = await $api('/api/accounts/login/', {
        method: 'POST',
        body: credentials,
      })
      if (response.failed) {
        return response
      }

      useUserStore().setSelfInfo(response.data)
      this.setAuthenticated(true)
      return response
    },

    async logout() {
      const { $api } = useNuxtApp()
      await $api('/api/accounts/logout/', {method: 'POST'})

      useUserStore().setSelfInfo()
      this.setAuthenticated(false)
    },

    async register(data) {
      const { $api } = useNuxtApp()
      const response = await $api('/api/accounts/account/', {
        method: 'POST',
        body: data,
      })

      if (!response.failed) {
        await navigateTo(
          {
            path: '/auth/login',
            query: {
              new: true
            }
          },
          {
            redirectCode: 301,
          }
        )
        return {}
      }
      return response.data
    },

    async update(data: AccountUpdateData) {
      const { $api } = useNuxtApp()
      const requestBody = {
        email: data.email,
        first_name: data.first_name,
        last_name: data.last_name,
      }
      if (data.password1 || data.password2) {
        requestBody.password1 = data.password1
        requestBody.password2 = data.password2
      }
      const response = await $api('/api/accounts/account/', {
        method: 'PATCH',
        body: requestBody,
      })

      if (!response.failed) {
        await useUserStore().fetchSelfInfo()
      }
      return response
    },

    setAuthenticated(value: boolean) {
      this.isAuthenticated = value
    }
  }
})