<script setup>
import DefaultTheme from 'vitepress/theme'

const { Layout } = DefaultTheme
</script>

<template>
    <Layout>
        <template #not-found>
            <iframe src="/404.html" frameborder="0"
                style="width: 100%; height: 100dvh; max-height: calc(100dvh - 113px - 64px);"></iframe>
        </template>
    </Layout>
</template>