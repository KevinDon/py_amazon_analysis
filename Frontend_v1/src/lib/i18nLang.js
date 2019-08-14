import Vue from 'vue'
import VueI18n from 'vue-i18n'
import configs from '@/lib/sysConfig'

Vue.use(VueI18n);

const DEFAULT_LANG = configs.lang || 'zh'
console.log(DEFAULT_LANG);
const LOCALE_KEY = 'localeLanguage'

const locales = {
  zh: require('static/lang/zh.json'),
  en: require('static/lang/en.json'),
}

const i18n = new VueI18n({
  locale: DEFAULT_LANG,
  messages: locales,
})

export const setup = lang => {
  if (lang === undefined) {
    lang = window.localStorage.getItem(LOCALE_KEY)
    if (locales[lang] === undefined) {
      lang = DEFAULT_LANG
    }
  }
  window.localStorage.setItem(LOCALE_KEY, lang)

  Object.keys(locales).forEach(lang => {
    document.body.classList.remove(`lang-${lang}`)
  })
  document.body.classList.add(`lang-${lang}`)
  document.body.setAttribute('lang', lang)

  Vue.config.lang = lang
  i18n.locale = lang
}

setup()
export default i18n
