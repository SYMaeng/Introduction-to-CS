module.exports = {
    async rewrites() {
        return [
            {
                source: '/processing',
                destination: '/processing.html',
            },
        ]
    },
}
