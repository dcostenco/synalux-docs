# Team Chat & Communication

## Secure Messaging

HIPAA-compliant real-time messaging between team members. End-to-end encrypted channels with configurable message retention policies and audit trails.

## Channels & Groups

Create topic-based channels (e.g., #clinical, #billing, #urgent) and direct message groups. Channel-level access controls for sensitive clinical discussions.

## File Sharing

Share documents, images, and clinical resources within chat. Files inherit workspace-level encryption and access controls for HIPAA compliance.

## Notifications

Configurable notification preferences per channel. @mentions, urgent flags, and do-not-disturb scheduling for work-life balance and emergency escalation.

## Enterprise Video Calls (LiveKit SFU)

Synalux Enterprise utilizes a state-of-the-art **Selective Forwarding Unit (SFU)** powered by LiveKit to provide seamless, high-definition real-time communication (RTC) across both the Next.js Web Portal and the native VS Code Extension Webview. 

### 📊 Enterprise Capacity & Quotas

| Feature | Synalux Standard | Synalux Enterprise | Notes |
| :--- | :--- | :--- | :--- |
| **Concurrent Participants** | Up to 8 per room | **25+ (Scales to 100)** | Fully supports large clinical scrums and all-hands. |
| **Daily Call Limits** | Unlimited | **Unlimited** | No hard caps on daily connection generation. |
| **Maximum Call Duration** | Unlimited | **Unlimited** | JWT tokens are seamlessly refreshed in the background. |
| **Video Resolution** | 720p HD | **1080p FHD** | Handled dynamically via WebRTC Simulcast. |
| **Upstream Bandwidth** | `O(1)` | **`O(1)`** | Users upload exactly **1** stream, regardless of room size. |

### 🔒 Cross-Practice Data Isolation
Room generation is cryptographically bound:
* **Workspace Channels:** Rooms are strictly generated as `ws_${workspaceId}_channel_${channelId}`.
* **Encrypted Direct Messages:** Cross-practice DMs utilize an isolated `dm_thread_${channelId}` nomenclature, ensuring isolated 1-on-1 calls without compromising workspace-level ACLs.
