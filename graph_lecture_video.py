"""
graph_lecture_video.py  —  MAIN ENTRY POINT
Run:  python graph_lecture_video.py

Requirements:
    pip install moviepy matplotlib pillow numpy networkx

Outputs:
    graph_video/frames/  — individual PNG frames
    Graph_Theory_Lecture.mp4  — final video (~83 min at 24fps)

Each scene is rendered at 1920×1080 (120 dpi × 16×9 in).
"""

import os, sys, glob, shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── output directories ────────────────────────────────────────────────────────
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
FRAMES_DIR = os.path.join(BASE_DIR, "graph_video", "frames")
os.makedirs(FRAMES_DIR, exist_ok=True)

# ensure local module path
sys.path.insert(0, os.path.join(BASE_DIR, "graph_video"))

from scenes_1_foundations  import (s01_cold_open, s02_konigsberg,
                                    s03_graph_anatomy, s04_matrices,
                                    s05_adjacency_list, s06_walks,
                                    s07_connectivity)
from scenes_2_special_graphs import (s08_complete_graph, s09_cycle_wheel,
                                      s10_hypercube, s11_bipartite,
                                      s12_isomorphism)
from scenes_3_algorithms     import (s13_euler_hierholzer, s14_bfs_dfs,
                                      s15_prims, s16_kruskals,
                                      s17_dijkstra, s18_planar)

# ── scene registry ────────────────────────────────────────────────────────────
SCENES = [
    ("01_cold_open",         s01_cold_open),
    ("02_konigsberg",        s02_konigsberg),
    ("03_graph_anatomy",     s03_graph_anatomy),
    ("04_matrices",          s04_matrices),
    ("05_adj_list",          s05_adjacency_list),
    ("06_walks",             s06_walks),
    ("07_connectivity",      s07_connectivity),
    ("08_complete_graph",    s08_complete_graph),
    ("09_cycle_wheel",       s09_cycle_wheel),
    ("10_hypercube",         s10_hypercube),
    ("11_bipartite",         s11_bipartite),
    ("12_isomorphism",       s12_isomorphism),
    ("13_euler",             s13_euler_hierholzer),
    ("14_bfs_dfs",           s14_bfs_dfs),
    ("15_prims",             s15_prims),
    ("16_kruskals",          s16_kruskals),
    ("17_dijkstra",          s17_dijkstra),
    ("18_planar",            s18_planar),
]

# ── transition frame ──────────────────────────────────────────────────────────
TRANSITION_TITLES = {
    "01_cold_open":      "Graph Theory & Algorithms",
    "02_konigsberg":     "§1 · The Königsberg Problem",
    "03_graph_anatomy":  "§2 · Graph Anatomy: G = (V, E)",
    "04_matrices":       "§3 · Adjacency & Laplacian Matrices",
    "05_adj_list":       "§3 · Adjacency List",
    "06_walks":          "§4 · Walks · Trails · Paths · Circuits",
    "07_connectivity":   "§5 · Connectivity & Bridges",
    "08_complete_graph": "§6 · Complete Graph Kₙ",
    "09_cycle_wheel":    "§6 · Cycle Cₙ & Wheel Wₙ",
    "10_hypercube":      "§6 · Hypercube Qₙ",
    "11_bipartite":      "§6 · Bipartite & K_{m,n}",
    "12_isomorphism":    "§7 · Graph Isomorphism",
    "13_euler":          "§8 · Eulerian Circuits: Hierholzer's",
    "14_bfs_dfs":        "§9 · BFS & DFS Traversals",
    "15_prims":          "§10 · Prim's MST Algorithm",
    "16_kruskals":       "§10 · Kruskal's MST Algorithm",
    "17_dijkstra":       "§11 · Dijkstra's Shortest Paths",
    "18_planar":         "§12 · Planar Graphs & Euler's Formula",
}

def make_transition(title, out_path):
    """Render 24 fade-in/out title frames for a scene transition."""
    from scene_utils import BG, CYAN, GOLD, WHITE
    N = 24
    for i in range(N):
        t = i/(N-1)
        alpha = np.sin(t * np.pi)        # 0→1→0
        fig, ax = plt.subplots(figsize=(16,9), facecolor=BG)
        ax.set_facecolor(BG); ax.axis("off")
        ax.set_xlim(0,16); ax.set_ylim(0,9)
        ax.text(8, 4.8, title, color=CYAN, fontsize=28,
                ha="center", va="center", fontweight="bold", alpha=alpha)
        ax.text(8, 3.8, "Graph Theory & Algorithms", color=GOLD,
                fontsize=14, ha="center", va="center", alpha=alpha*0.6)
        fig.savefig(f"{out_path}/tr_{i:04d}.png", dpi=120,
                    facecolor=BG, bbox_inches="tight", pad_inches=0)
        plt.close(fig)

# ── render all scenes ─────────────────────────────────────────────────────────
def render_all(skip_existing=True):
    print("=" * 60)
    print("  Graph Theory Lecture Video — Frame Renderer")
    print("=" * 60)
    for scene_id, scene_fn in SCENES:
        scene_dir = os.path.join(FRAMES_DIR, scene_id)
        os.makedirs(scene_dir, exist_ok=True)
        existing = glob.glob(os.path.join(scene_dir, "*.png"))
        if skip_existing and existing:
            print(f"  [SKIP] {scene_id}  ({len(existing)} frames exist)")
            continue
        print(f"  [RENDER] {scene_id} ...", end="", flush=True)
        try:
            scene_fn(scene_dir)
            count = len(glob.glob(os.path.join(scene_dir, "*.png")))
            print(f"  ✓  {count} frames")
        except Exception as e:
            print(f"  ✗  ERROR: {e}")
            import traceback; traceback.print_exc()

# ── assemble video ────────────────────────────────────────────────────────────
def assemble_video(fps=24, output="Graph_Theory_Lecture.mp4"):
    try:
        from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
        from moviepy.editor import concatenate_videoclips
    except ImportError:
        print("moviepy not found. Run:  pip install moviepy")
        return

    clips = []
    for scene_id, _ in SCENES:
        # transition
        tr_dir = os.path.join(FRAMES_DIR, f"_tr_{scene_id}")
        os.makedirs(tr_dir, exist_ok=True)
        if not glob.glob(os.path.join(tr_dir, "*.png")):
            title = TRANSITION_TITLES.get(scene_id, scene_id)
            make_transition(title, tr_dir)
        tr_frames = sorted(glob.glob(os.path.join(tr_dir, "*.png")))
        if tr_frames:
            clips.append(ImageSequenceClip(tr_frames, fps=fps))

        # scene frames
        scene_dir   = os.path.join(FRAMES_DIR, scene_id)
        scene_frames = sorted(glob.glob(os.path.join(scene_dir, "*.png")))
        if not scene_frames:
            print(f"  [WARN] No frames for scene {scene_id}")
            continue
        clips.append(ImageSequenceClip(scene_frames, fps=fps))
        print(f"  [CLIP] {scene_id}  ({len(scene_frames)} frames @ {fps}fps = {len(scene_frames)/fps:.1f}s)")

    if not clips:
        print("No clips to assemble.")
        return

    print(f"\nConcatenating {len(clips)} clips …")
    final = concatenate_videoclips(clips, method="compose")
    out_path = os.path.join(BASE_DIR, output)
    final.write_videofile(out_path, fps=fps, codec="libx264",
                          audio=False, logger="bar")
    print(f"\n✅  Video saved to: {out_path}")
    print(f"   Duration: {final.duration/60:.1f} minutes")

# ── closing scene ─────────────────────────────────────────────────────────────
def render_closing(out_dir):
    """Simple closing credits scene."""
    from scene_utils import BG, CYAN, GOLD, WHITE, GREEN, CORAL, GRAY
    os.makedirs(out_dir, exist_ok=True)
    topics = [
        "Graph Anatomy  G=(V,E)",
        "Special Graphs: Kₙ, Cₙ, Wₙ, Qₙ, K_{m,n}",
        "Isomorphism & Invariants",
        "Eulerian Circuits: Hierholzer's  O(V+E)",
        "Hamiltonian Circuits & TSP",
        "Planar Graphs & Euler's Formula",
        "BFS & DFS  O(V+E)",
        "Prim's MST  O((V+E) log V)",
        "Kruskal's MST  O(E log E)",
        "Dijkstra's SSSP  O((V+E) log V)",
    ]
    STEPS = 60
    for step in range(STEPS):
        t = step/(STEPS-1)
        fig, ax = plt.subplots(figsize=(16,9), facecolor=BG)
        ax.set_facecolor(BG); ax.axis("off")
        ax.set_xlim(0,16); ax.set_ylim(0,9)

        ax.text(8,8.3,"Graph Theory & Algorithms — Complete",
                color=CYAN,fontsize=24,ha="center",fontweight="bold",alpha=min(1,t*3))
        ax.text(8,7.6,"Topics Covered:",
                color=GOLD,fontsize=14,ha="center",alpha=min(1,t*3))

        for i,topic in enumerate(topics):
            ta = max(0, min(1, (t*2 - i*0.15)))
            ax.text(8, 6.8 - i*0.58, f"✓  {topic}",
                    color=WHITE,fontsize=11,ha="center",alpha=ta)

        ax.text(8,0.6,"Graphs power the internet, GPS, social networks & more.",
                color=GREEN,fontsize=11,ha="center",alpha=min(1,max(0,(t-0.7)*4)),
                style="italic")
        fig.savefig(f"{out_dir}/closing_{step:04d}.png", dpi=120,
                    facecolor=BG, bbox_inches="tight", pad_inches=0)
        plt.close(fig)

# ── CLI ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Graph Theory Lecture Video Generator")
    parser.add_argument("--skip-existing", action="store_true", default=True,
                        help="Skip re-rendering scenes that already have frames")
    parser.add_argument("--render-only", action="store_true",
                        help="Only render frames, do not assemble video")
    parser.add_argument("--assemble-only", action="store_true",
                        help="Only assemble video from existing frames")
    parser.add_argument("--scene", type=str, default=None,
                        help="Render a single scene by ID (e.g. 14_bfs_dfs)")
    parser.add_argument("--fps", type=int, default=24,
                        help="Frames per second for output video (default: 24)")
    parser.add_argument("--output", type=str, default="Graph_Theory_Lecture.mp4",
                        help="Output video filename")
    args = parser.parse_args()

    if args.scene:
        # render just one scene
        scene_map = {sid: fn for sid, fn in SCENES}
        if args.scene not in scene_map:
            print(f"Unknown scene: {args.scene}")
            print("Available:", list(scene_map.keys()))
            sys.exit(1)
        scene_dir = os.path.join(FRAMES_DIR, args.scene)
        os.makedirs(scene_dir, exist_ok=True)
        print(f"Rendering single scene: {args.scene}")
        scene_map[args.scene](scene_dir)
        count = len(glob.glob(os.path.join(scene_dir, "*.png")))
        print(f"Done: {count} frames in {scene_dir}")
    elif args.assemble_only:
        # render closing then assemble
        render_closing(os.path.join(FRAMES_DIR, "19_closing"))
        assemble_video(fps=args.fps, output=args.output)
    elif args.render_only:
        render_all(skip_existing=args.skip_existing)
        render_closing(os.path.join(FRAMES_DIR, "19_closing"))
    else:
        # default: render + assemble
        render_all(skip_existing=args.skip_existing)
        render_closing(os.path.join(FRAMES_DIR, "19_closing"))
        assemble_video(fps=args.fps, output=args.output)
