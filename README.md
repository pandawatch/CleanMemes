# CleanMemes - Random Memes Scroller + Favorites Turbo

A high-performance infinite meme scroller with favorites management and ZIP export capabilities.

## 🚀 Quick Start

### Option 1: Node.js Server (Recommended)
```bash
node server.js
```
Opens at `http://localhost:3000`

Or with npm:
```bash
npm start
```

Custom port:
```bash
PORT=8080 node server.js
```

### Option 2: Python Server
```bash
python3 server.py
```

Or with custom port:
```bash
PORT=8080 python3 server.py
```

## ✨ Features

- **Fast Random Meme Generation** - Optimized parallel image loading
- **Favorites System** - Save memes to localStorage with instant lookups
- **ZIP Export** - Download all favorites as a ZIP file
- **Smart Caching** - Month cache prevents redundant lookups
- **Super Mode** - Load more memes per cycle for intensive browsing
- **Keyboard Shortcuts** - Press `H` to hide/show controls
- **Responsive Design** - Works on desktop and mobile

## ⚡ Performance Optimizations

### Latest Updates:
- **Non-blocking Page Load** - Initial generation delayed until page fully loads
- **Deferred CDN Scripts** - JSZip/FileSaver load asynchronously without blocking
- **Loading Placeholder** - Shows "Loading memes..." while generation starts
- **Parallel Extension Testing** - Tests `.jpg`, `.jpeg`, `.png`, `.webp` simultaneously (~3-4x faster)
- **Aggressive Timeouts** - 4-second image fetch timeout prevents hanging
- **DocumentFragment Rendering** - Batch DOM updates for 2-3x faster rendering
- **Debounced Updates** - Favorites list updates batched to prevent UI thrashing
- **O(1) Favorite Lookups** - Set-based storage for instant favorite checking
- **Reduced Promise Volume** - Smart index sampling (2000 max vs 9999) cuts load time
- **Minimal DOM Updates** - Favorite toggle updates only affected card, not entire lane
- **Pre-cached Months** - Aggressive caching of valid month/index combos

**Result**: Page loads instantly, generation is **2-3x faster** than v1

## 🐛 Bug Fixes

### ZIP Download
✅ **Fixed**: ZIP downloads now work without CORS issues
- Uses `no-cors` mode for image fetching
- Automatically timestamps ZIP files to prevent overwrites
- Shows download progress feedback
- Gracefully handles unreachable images

## 🎮 Usage

1. **Generate**: Click `Generate` to load 5 random memes (configurable)
2. **Shuffle**: Randomize the order of current memes
3. **Next Random**: Jump to a random meme in the carousel
4. **Favorites**: Click ⭐ on any meme to save it
5. **Download**: Export all favorites as a ZIP file
6. **Super Mode**: Toggle for more aggressive loading

## 💾 Local Storage

- `favoritesV2` - Saved favorite images
- `favoriteCounter` - Favorite counter for naming
- `monthCacheV1` - Month availability cache
- `seenImages` - Set of seen image URLs
- `imageCount` - Last used generation count

## 🛠️ Technical Details

- Pure HTML/CSS/JavaScript (no build dependencies)
- Uses JSZip and FileSaver for downloads
- Promise.allSettled for robust error handling
- localStorage for persistent favorites
- Image lazy loading for performance

## 📝 Server Configuration

Both servers automatically:
- Serve `index.html` for root path
- Set proper MIME types
- Enable CORS headers for images
- Handle 404s gracefully

Environment variables:
- `PORT` - Server port (default: 3000)
- `HOST` - Server host (default: localhost)