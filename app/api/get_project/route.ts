import { NextResponse } from 'next/server';
import supabase from "@/lib/supabase";

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const projectId = searchParams.get('projectId');

  try {
    const { data, error } = await supabase
      .from('Projects')
      .select(`
        id,
        title,
        progression,
        Steps(title, tools, action, raw_img)
      `)
      .eq('id', projectId);
    
    if (error) {
      console.error("Error from the project fetch:", error);
      return NextResponse.json({ error: error.message }, { status: 500 });
    }
    
    if (data) {
      return NextResponse.json(data);
    }

    return NextResponse.json({ error: "No data found" }, { status: 404 });

  } catch (error) {
    console.error("Error retrieving project:", error);
    return NextResponse.json(
      { error: "An error occurred while retrieving the project." }, 
      { status: 500 }
    );
  }
}