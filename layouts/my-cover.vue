<script setup>
import { computed } from 'vue'

defineProps({
  date: { type: String, default: '2026-02-21' },
  author: { type: String, default: '' },
  affiliation: { type: String, default: '' },
  email: { type: String, default: '' },
  seriesName: { type: String, default: '' },
})
</script>

<template>
  <div class="cover-layout">
    <!-- Top row: series label (left) + date (right) -->
    <div class="cover-top">
      <div v-if="seriesName || $slidev.configs.title" class="series-label">
        {{ seriesName || $slidev.configs.title }}
      </div>
      <div class="cover-date">{{ date }}</div>
    </div>

    <!-- Center: main title slot -->
    <div class="cover-center">
      <slot />
    </div>

    <!-- Dotted separator line -->
    <div class="cover-separator"></div>

    <!-- Author info row -->
    <div v-if="author || $slidev.configs.author || affiliation || email" class="cover-author-row">
      <div v-if="author || $slidev.configs.author" class="cover-author-name">{{ author || $slidev.configs.author }}</div>
      <div v-if="affiliation || $slidev.configs.affiliation" class="cover-author-affiliation">{{ affiliation || $slidev.configs.affiliation }}</div>
      <div v-if="email" class="cover-author-email">{{ email }}</div>
    </div>

    <!-- Bottom-right: CC BY-NC placeholder -->
    <div class="cover-cc">CC BY-NC</div>
  </div>
</template>
