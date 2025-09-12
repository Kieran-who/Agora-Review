<script setup>
import DefaultTheme from 'vitepress/theme'

const { Layout } = DefaultTheme
</script>

<template>
    <Layout>
        <template #not-found>
            <iframe src="/404.html" frameborder="0" style="width: 100%; height: 100dvh;"></iframe>
        </template>
    </Layout>
</template>