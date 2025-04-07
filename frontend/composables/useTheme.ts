// noinspection JSUnusedGlobalSymbols
export default function useTheme() {
    const isDarkMode = useState<boolean | null>('theme', () => null)

    onMounted(() => {
        isDarkMode.value = localStorage.getItem('theme') === 'dark'
    })

    const toggleDarkMode = () => {
        isDarkMode.value = !isDarkMode.value
        localStorage.setItem('theme', isDarkMode.value ? 'dark' : 'light')

        const theme = localStorage.getItem('theme')
        if (!theme || theme === 'dark') {
            document.documentElement.classList.add('p-dark')
        } else {
            document.documentElement.classList.remove('p-dark')
        }
    }

    return {
        isDarkMode,
        toggleDarkMode,
    }
}