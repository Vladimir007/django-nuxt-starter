import { defineStore } from "pinia"

interface SelfInfo {
  id?: number;
  is_staff: boolean;
  email: string;
  first_name: string;
  last_name: string;
}

// noinspection JSUnusedGlobalSymbols
export const useUserStore = defineStore('user', {
  state: () => ({
    loaded: false,
    id: null,
    is_staff: false,
    email: '',
    first_name: '',
    last_name: '',
  }),
  getters: {
    label: (state) => state.first_name[0] + state.last_name[0],
  },
  actions: {
    async fetchSelfInfo() {
      const { $api } = useNuxtApp()
      const { failed, data } = await $api('/api/accounts/account/')

      if (!failed) {
        this.setSelfInfo(data)
        useAuthStore().setAuthenticated(true)
      }
    },

    setSelfInfo(data: SelfInfo = null) {
      this.loaded = true
      this.id = data?.id
      this.is_staff = data?.is_staff || false
      this.email = data?.email || ""
      this.first_name = data?.first_name || ""
      this.last_name = data?.last_name || ""
    }
  }
})