<script setup lang="ts">
definePageMeta({
  layout: 'auth'
})

const toast = useToast()

const loading = ref(false)
const authStore = useAuthStore()

const formData = reactive({
  email: authStore.user.email,
  first_name: authStore.user.first_name,
  last_name: authStore.user.last_name,
  password1: "",
  password2: "",
})

const formErrors = ref(null)

const handleSubmit = async () => {
  loading.value = true
  formErrors.value = await authStore.updateUser(formData)
  if (formErrors.value?.detail) {
    toast.add({ severity: 'error', summary: 'Error', detail: formErrors.value.detail })
  } else if (!formErrors.value) {
    toast.add({ severity: 'success', summary: 'Success', detail: "Profile was successfully updated", life: 2000 })
  }
  loading.value = false
}
</script>

<template>
  <Card fluid>
    <template #title>Profile</template>
    <template #content>
      <form @submit.prevent="handleSubmit" class="flex flex-col gap-4">
        <AuthFormField v-model="formData.email" name="email" label="Email" :errors="formErrors?.email" />
        <AuthFormField v-model="formData.first_name" name="first_name" label="First name" :errors="formErrors?.first_name" />
        <AuthFormField v-model="formData.last_name" name="last_name" label="Last name" :errors="formErrors?.last_name" />
        <AuthFormField v-model="formData.password1" name="password1" label="Password" type="password" :errors="formErrors?.password1" />
        <AuthFormField v-model="formData.password2" name="password2" label="Password confirmation" type="password" :errors="formErrors?.password2" />

        <Message v-if="formErrors?.general" severity="error" size="small">
          <ul class="my-0 px-4 flex flex-col gap-1">
            <li v-for="(error, index) of formErrors.general" :key="index">{{ error }}</li>
          </ul>
        </Message>

        <Button :loading type="submit" severity="secondary" label="Submit" />
      </form>

      <Divider layout="horizontal" align="center"><b>OR</b></Divider>
      <Button severity="primary" v-slot="slotProps" fluid asChild>
        <NuxtLink to="/" :class="slotProps.class">Back to Home</NuxtLink>
      </Button>
    </template>
  </Card>
</template>