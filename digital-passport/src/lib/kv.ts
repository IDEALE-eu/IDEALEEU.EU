// Simple browser-local storage implementation (Spark KV API mock)
export class SparkKV {
  private prefix: string

  constructor(namespace: string) {
    this.prefix = `spark_kv_${namespace}_`
  }

  get<T>(key: string): T | null {
    const item = localStorage.getItem(this.prefix + key)
    if (!item) return null
    try {
      return JSON.parse(item) as T
    } catch {
      return null
    }
  }

  set<T>(key: string, value: T): void {
    localStorage.setItem(this.prefix + key, JSON.stringify(value))
  }

  delete(key: string): void {
    localStorage.removeItem(this.prefix + key)
  }

  keys(): string[] {
    const keys: string[] = []
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i)
      if (key && key.startsWith(this.prefix)) {
        keys.push(key.substring(this.prefix.length))
      }
    }
    return keys
  }

  clear(): void {
    const keys = this.keys()
    keys.forEach(key => this.delete(key))
  }
}

export const passportKV = new SparkKV('digital-passports')
export const templateKV = new SparkKV('templates')
