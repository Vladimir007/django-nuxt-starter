<script setup lang="ts">
definePageMeta({
  layout: 'auth'
})

// Get CSRF when page is loaded
const { $api } = useNuxtApp()
onMounted(() => {
  $api('/api/accounts/login/')
})

const route = useRoute()

const loading: Ref<boolean> = ref(false)

const formData: Reactive<ICredentials> = reactive({
  email: "",
  password: "",
})
const error = ref()

const handleSubmit = async () => {
  loading.value = true
  error.value = await useAuthStore().login(formData)
  loading.value = false
}
</script>

<template>
  <Card>
    <template #title>Login</template>
    <template #content>
      <form @submit.prevent="handleSubmit" class="flex flex-col gap-4">
        <Message v-if="route.query.new === 'true'" severity="warn">Please contact administrator to activate your account</Message>
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
