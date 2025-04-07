<script setup lang="ts">
const model = defineModel()
defineProps<{
  label: string
  name: string
  type?: string
  errors?: string[]
  disabled?: boolean
}>()
</script>

<template>
  <div class="flex flex-col gap-1">
    <FloatLabel variant="on">
      <InputText :id="name" v-model="model" :invalid="!!errors" :disabled="disabled || false" :name="name" :type="type || 'text'" fluid />
      <label :for="name">{{ label }}</label>
    </FloatLabel>
    <Message v-if="errors" severity="error" size="small" variant="simple">
      <ul class="my-0 px-4 flex flex-col gap-1">
        <li v-for="(error, index) of errors" :key="index">{{ error }}</li>
      </ul>
    </Message>
  </div>
</template>
