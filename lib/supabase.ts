import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://hcrkjwcuigvggxkipdsj.supabase.co'
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imhjcmtqd2N1aWd2Z2d4a2lwZHNqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzY2MjY0ODMsImV4cCI6MjA1MjIwMjQ4M30.QvVRnjvDNdSIPJ07kwApwcVN28He-M1uJjhMFaTrFkk'
const supabase = createClient(supabaseUrl, supabaseKey)

export default supabase;