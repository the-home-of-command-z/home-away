const { WebClient } = require('@slack/web-api');

const web = new WebClient(process.env.SLACK_TOKEN);

const currentTime = new Date().toTimeString();

(async () => {
    const res = await web.auth.test()

    const userId = res.user_id

    await web.chat.postMessage({
        channel: 'general',
        text: `The current time is ${currentTime}`,
    });

    console.log('Message posted!');
})();