<!--suppress VueUnrecognizedDirective -->
<script setup lang="ts">

const toast = useToast()
const { isDarkMode, toggleDarkMode } = useTheme()
const authStore = useAuthStore()

const navItems = [
  {
    label: 'Home',
    icon: 'pi pi-home',
    route: '/'
  },
  {
    label: 'Test',
    icon: 'pi pi-play',
    command: async () => {
      const { $api } = useNuxtApp()
      const data = await $api('/api/accounts/test/', {method: "POST"}).catch(({ data }) => {
        toast.add({ severity: 'error', summary: 'Error', detail: data.detail || "Test request finished with error" })
        return null
      })
      if (data) {
        toast.add({ severity: 'success', summary: 'Success', detail: data.detail, life: 2000 })
      }
    }
  },
]

if (authStore.user.is_staff) {
  navItems.push({
    label: 'Admin page',
    icon: 'pi pi-database',
    url: '/admin/'
  })
}

const userMenu = ref();

const userMenuItems = ref([
  {
    label: "Profile",
    icon: "pi pi-user-edit",
    route: "/auth/profile"
  },
  {
    label: "Logout",
    icon: "pi pi-sign-out",
    command: async () => {
      await authStore.logout()
    }
  }
])
const showUserMenu = (event) => {
  userMenu.value.toggle(event)
}
</script>

<template>
  <Menubar :model="navItems">
    <template #item="{ item, props, hasSubmenu }">
        <NuxtLink v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
            <a v-ripple :href="href" v-bind="props.action" @click="navigate">
                <span :class="item.icon" />
                <span>{{ item.label }}</span>
            </a>
        </NuxtLink>
        <a v-else v-ripple :href="item.url" :target="item.target" v-bind="props.action">
            <span :class="item.icon" />
            <span>{{ item.label }}</span>
            <span v-if="hasSubmenu" class="pi pi-fw pi-angle-down" />
        </a>
    </template>
    <template #end>
      <div class="flex flex-row">
        <Button icon="pi pi-user" aria-label="User menu" aria-haspopup="true" aria-controls="user_menu" severity="contrast" variant="text" rounded @click="showUserMenu"/>
        <Button :icon="'pi ' + (isDarkMode ? 'pi-moon': 'pi-sun')" aria-label="Switch dark mode" severity="contrast" variant="text" rounded @click="toggleDarkMode"/>
      </div>
    </template>
  </Menubar>

  <Menu ref="userMenu" id="user_menu" :model="userMenuItems" :popup="true">
    <template #start>
      <span class="w-full flex p-4 pr-8">
        <Avatar :label="authStore.userLabel" class="mr-3 bg-violet-200! dark:bg-violet-900!" size="large" shape="circle" />
        <span class="flex flex-col">
          <span class="font-bold">{{ authStore.user.first_name }} {{ authStore.user.last_name }}</span>
          <span class="text-sm italic">{{ authStore.user.email }}</span>
        </span>
      </span>
    </template>
    <template #item="{ item, props }">
      <NuxtLink v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
          <a class="flex items-center" v-bind="props.action" :href="href" @click="navigate">
              <span :class="item.icon" />
              <span>{{ item.label }}</span>
          </a>
      </NuxtLink>
      <a v-else class="flex items-center" v-bind="props.action">
          <span :class="item.icon" />
          <span>{{ item.label }}</span>
      </a>
    </template>
  </Menu>
</template>
