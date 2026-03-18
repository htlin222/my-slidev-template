<script setup>
import { computed } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'
import { slides } from '#slidev/slides'

const { go } = useNav()
const { $page } = useSlideContext()

/** Dynamically compute chapters from h1 slides (skip slide 1 = cover) */
const chapters = computed(() => {
  const allSlides = slides.value
  if (!allSlides) return []

  const h1Slides = []
  for (const slide of allSlides) {
    const info = slide.meta?.slide
    if (!info) continue
    if (info.level === 1 && slide.no > 1) {
      h1Slides.push({ label: info.title || '', start: slide.no })
    }
  }

  return h1Slides
})

/** Use injected $page (stable per-slide) instead of reactive currentSlideNo to prevent shrink-before-fade */
const sectionIndex = computed(() => {
  return chapters.value.findIndex(ch => ch.start === $page.value)
})
</script>

<template>
  <div class="section-layout">
    <!-- Top-left: section label -->
    <div class="section-label">
      Section: {{ sectionIndex + 1 }}
    </div>

    <!-- Main content area with chapter list -->
    <div class="section-content">
      <ol class="chapter-list">
        <li
          v-for="(chapter, index) in chapters"
          :key="chapter.label"
          :class="['chapter-item', { active: index === sectionIndex }]"
          @click="go(chapter.start)"
        >
          <span class="chapter-number">{{ index + 1 }}.</span>
          <span class="chapter-text">{{ chapter.label }}</span>
        </li>
      </ol>
    </div>

  </div>
</template>
