<script setup lang="ts">
definePageMeta({
  layout: 'auth'
})

// Get CSRF when page is loaded
const { $api } = useNuxtApp()
onMounted(() => {
  $api('/api/accounts/login/')
})

// Whether user just registered or not
const route = useRoute()
const isUserNew = route.query.new === 'true'

const loading = ref(false)

const formData = reactive({
  email: "",
  password: "",
})
const error = ref(null)

const handleSubmit = async () => {
  loading.value = true
  error.value = null

  const { data, failed } = await useAuthStore().login(formData)
  if (failed) {
    error.value = data.detail
  } else {
    formData.email = ""
    formData.password = ""
    navigateTo(route.query.next || '/', {redirectCode: 301})
  }

  loading.value = false
}

</script>

<template>
  <Card>
    <template #title>Login</template>
    <template #content>
      <form @submit.prevent="handleSubmit" class="flex flex-col gap-4">
        <Message v-if="isUserNew" severity="warn">Please contact administrator to activate your account</Message>
        <AuthFormField v-model="formData.email" name="email" label="Email" />
        <AuthFormField v-model="formData.password" name="password" type="password" label="Password" />
        <Message v-if="error" severity="error" size="small">{{ error }}</Message>
        <Button :loading type="submit" severity="secondary" label="Submit" fluid />
      </form>

      <Divider layout="horizontal" align="center"><b>OR</b></Divider>
      <Button severity="primary" v-slot="slotProps" fluid asChild>
        <NuxtLink to="/auth/register" :class="slotProps.class">Sign up</NuxtLink>
      </Button>
    </template>
  </Card>
</template>
