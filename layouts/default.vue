<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'
import { slides } from '#slidev/slides'
import Chapter from './chapter.vue'

const { $page } = useSlideContext()

const isChapter = computed(() => {
  const allSlides = slides.value
  if (!allSlides) return false
  const current = allSlides.find(s => s.no === $page.value)
  return current?.meta?.slide?.level === 1 && $page.value > 1
})
</script>

<template>
  <Chapter v-if="isChapter" />
  <div v-else class="slidev-layout default">
    <slot />
  </div>
</template>
